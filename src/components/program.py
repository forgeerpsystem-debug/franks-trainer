import streamlit as st
import json
import os

def load_program_data():
    file_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "program.json")
    with open(file_path, "r") as f:
        return json.load(f)

def render():
    st.header("📋 The Plan")
    
    program_data = load_program_data()
    
    # Dropdown to select the current day
    day_selected = st.selectbox("Select Training Day", options=list(program_data.keys()), label_visibility="collapsed")
    
    st.divider()
    
    # Fetch the specific workout data for the selected day
    exercises = program_data[day_selected]
    
    # Render mobile-friendly cards for each movement
    for ex in exercises:
        with st.container(border=True):
            st.subheader(ex["name"])
            
            # Use columns to stack metrics cleanly on a phone
            cols = st.columns(3)
            cols[0].metric("Sets", ex["sets"])
            cols[1].metric("Reps", ex["reps"])
            cols[2].metric("Target", ex["target"])
            
            # App note for form and execution
            st.info(f"💡 **Note:** {ex['notes']}")
