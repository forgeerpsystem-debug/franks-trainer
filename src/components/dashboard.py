import streamlit as st
import pandas as pd
from datetime import datetime
from src.database import get_workout_history, get_exercises, get_exercise_history

def render(user_id: str):
    # ==========================================
    # SECTION 1: DAILY VOLUME (TONNAGE)
    # ==========================================
    st.header("Daily Volume")
    
    # Fetch raw data from Supabase
    raw_data = get_workout_history(user_id)
    
    if not raw_data:
        st.info("No workout data found yet. Log a session to see your stats here!")
    else:
        # Process and calculate math
        processed = []
        for row in raw_data:
            # Extract the timestamp from the joined workout_logs table
            date_str = row['workout_logs']['created_at']
            # Convert UTC ISO string to a clean local Date object
            date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00')).date()
            
            weight_kg = float(row['weight'])
            reps = int(row['reps'])
            
            # Calculate raw volume for this specific set
            volume_kg = weight_kg * reps
            
            processed.append({
                "Date": date_obj,
                "Volume_Kg": volume_kg
            })
            
        df = pd.DataFrame(processed)
        
        # Group by Date to get total daily tonnage
        daily_volume = df.groupby("Date")["Volume_Kg"].sum().reset_index()
        daily_volume = daily_volume.sort_values(by="Date", ascending=False)
        
        # Convert kg to lbs (1 kg = 2.20462 lbs)
        daily_volume["Volume_Lbs"] = daily_volume["Volume_Kg"] * 2.20462
        
        # Render Mobile-Friendly UI Cards
        st.write("👉 *Total Tonnage (Weight × Reps)*")
        
        for _, row in daily_volume.iterrows():
            with st.container(border=True):
                st.subheader(row["Date"].strftime("%b %d, %Y"))
                cols = st.columns(2)
                cols[0].metric(label="Total (Kg)", value=f"{row['Volume_Kg']:,.1f} kg")
                cols[1].metric(label="Total (Lbs)", value=f"{row['Volume_Lbs']:,.1f} lbs")


    st.divider()

    # ==========================================
    # SECTION 2: MOVEMENT HISTORY
    # ==========================================
    st.header("📜 Movement History")
    st.write("👉 *Select an exercise to view past sets*")
    
    exercises = get_exercises()
    
    if exercises:
        # Create dictionary of exercises and format the dropdown
        exercise_options = {f"{ex['name']} ({ex['category']})": ex['id'] for ex in exercises}
        selected_ex_name = st.selectbox("Target Movement", options=list(exercise_options.keys()), label_visibility="collapsed")
        selected_ex_id = exercise_options[selected_ex_name]
        
        # Fetch the specific history for this movement
        history_data = get_exercise_history(user_id, selected_ex_id)
        
        if history_data:
            processed_hist = []
            for row in history_data:
                # Parse date
                date_str = row['workout_logs']['created_at']
                date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                
                processed_hist.append({
                    "raw_date": date_obj, # Kept hidden just for strict chronological sorting
                    "Set": row["set_number"],
                    "Weight (kg)": float(row["weight"]),
                    "Reps": int(row["reps"])
                })
            
            # Sort chronologically by newest first, then clean up the date format for the UI
            processed_hist.sort(key=lambda x: x["raw_date"], reverse=True)
            for item in processed_hist:
                item["Date"] = item["raw_date"].strftime("%b %d")
                del item["raw_date"]
                
            df_hist = pd.DataFrame(processed_hist)
            
            # Reorder columns for a cleaner read on mobile
            df_hist = df_hist[["Date", "Set", "Weight (kg)", "Reps"]]
            
            # Render as a clean, index-free table
            st.dataframe(df_hist, use_container_width=True, hide_index=True)
        else:
            st.info("No logs found for this movement yet.")
    else:
        st.warning("No exercises in the database to display history for.")