import streamlit as st
from src.db.exercises import add_exercise, get_exercises

def render():
    st.header("⚙️ Manage Library")
    
    # 1. Add New Movement Form
    st.write("➕ **Add Custom Movement**")
    name = st.text_input("Exercise Name", placeholder="e.g., Deficit Deadlift")
    category = st.selectbox("Category", ["Lower Body", "Push", "Pull", "Shoulders", "Core", "Arms", "Cardio", "Other"])
    
    if st.button("Save Movement", type="primary", use_container_width=True):
        if name:
            if add_exercise(name, category):
                st.success(f"Added {name} to your library!")
                st.rerun() # Refresh to update the list below
            else:
                st.error("Failed to add exercise.")
        else:
            st.warning("Please enter a name.")
            
    st.divider()
    
    # 2. View Current Library
    st.write("📚 **Current Library**")
    exercises = get_exercises()
    
    if exercises:
        # Display the list cleanly on mobile
        for ex in sorted(exercises, key=lambda x: x['category']):
            st.markdown(f"• **{ex['name']}** *( {ex['category']} )*")