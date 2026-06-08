import streamlit as st
import pandas as pd
from datetime import datetime
from src.db.exercises import get_exercises
from src.db.workouts import save_workout, get_full_history
from src.components import timer

def render(user_id: str):
    # Handle success message from previous save
    if st.session_state.get("show_success"):
        st.success(st.session_state.show_success)
        st.session_state.show_success = False

    st.header("Log Session")
    
    # ==========================================
    # 1. EXERCISE SELECTOR
    # ==========================================
    exercises = get_exercises()
    if not exercises:
        st.warning("No exercises found. Seed your database.")
        return

    exercise_options = {f"{ex['name']} ({ex['category']})": ex['id'] for ex in exercises}
    selected_ex_name = st.selectbox("Movement", options=list(exercise_options.keys()))
    selected_ex_id = exercise_options[selected_ex_name]

    # ==========================================
    # 2. ASYNC REST TIMER
    # ==========================================
    st.write("") 
    timer.render()
    st.write("") 

    st.write("👉 *Tap cell to input weight & reps*")

    # ==========================================
    # 3. PHONE-OPTIMIZED DATA GRID
    # ==========================================
    # Setup standard 5-set structure default
    if "workout_df" not in st.session_state:
        st.session_state.workout_df = pd.DataFrame([
            {"Set": i, "Weight (kg)": 0.0, "Reps": 0} for i in range(1, 6)
        ])

    # Render the interactive grid
    edited_df = st.data_editor(
        st.session_state.workout_df,
        hide_index=True,
        num_rows="dynamic",
        use_container_width=True,
        column_config={
            "Set": st.column_config.NumberColumn("Set", disabled=True, width="small"),
            "Weight (kg)": st.column_config.NumberColumn("Weight", min_value=0.0, step=2.5, format="%.1f kg"),
            "Reps": st.column_config.NumberColumn("Reps", min_value=0, step=1)
        }
    )

    st.divider()
    notes = st.text_area("Notes (e.g., RPE, Form feel)", placeholder="Optional...")
    
    # ==========================================
    # 4. SAVE PIPELINE
    # ==========================================
    if st.button("Save Workout", type="primary", use_container_width=True):
        # Convert edited dataframe back to a list of dictionaries
        data_list = edited_df.to_dict(orient="records")
        
        with st.spinner("Uploading to Supabase..."):
            success, message = save_workout(
                user_id=user_id, 
                exercise_id=selected_ex_id, 
                sets_data=data_list, 
                notes=notes
            )
            
        if success:
            st.session_state.show_success = "Workout saved successfully! 💪"
            # Clear input state on successful save to prep for next exercise
            st.session_state.workout_df = pd.DataFrame([
                {"Set": i, "Weight (kg)": 0.0, "Reps": 0} for i in range(1, 6)
            ])
            st.rerun() # Refresh the UI instantly
        else:
            st.error(message)

    # ==========================================
    # 5. DAILY HISTORY
    # ==========================================
    st.divider()
    st.header("📜 Daily History")
    
    selected_date = st.date_input("Select Date", value=datetime.today())
    
    history_data = get_full_history(user_id)
    if history_data:
        daily_sets = []
        for row in history_data:
            date_str = row['workout_logs']['created_at']
            date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00')).date()
            if date_obj == selected_date:
                daily_sets.append({
                    "Movement": row['exercises']['name'] if row.get('exercises') else "Unknown",
                    "Set": row["set_number"],
                    "Weight (kg)": float(row["weight"]),
                    "Reps": int(row["reps"])
                })
        
        if daily_sets:
            df_daily = pd.DataFrame(daily_sets)
            st.dataframe(df_daily, use_container_width=True, hide_index=True)
        else:
            st.info(f"No workouts logged for {selected_date.strftime('%b %d, %Y')}.")
    else:
        st.info("No workout history found.")