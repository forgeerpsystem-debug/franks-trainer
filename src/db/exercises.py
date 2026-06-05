import streamlit as st
from src.db.core import supabase

@st.cache_data(ttl=3600)
def get_exercises():
    """Fetch the master list of exercises for the dropdowns."""
    try:
        response = supabase.table("exercises").select("*").execute()
        return response.data
    except Exception as e:
        print(f"Error fetching exercises: {e}")
        return []

def add_exercise(name: str, category: str):
    """Inserts a new custom exercise into the library."""
    try:
        supabase.table("exercises").insert({
            "name": name,
            "category": category
        }).execute()
        st.cache_data.clear() # Clear cache so the new exercise shows up
        return True
    except Exception as e:
        print(f"Error adding exercise: {e}")
        return False

def get_exercise_history(user_id: str, exercise_id: str):
    """Fetches every logged set for a specific exercise."""
    try:
        # We query set_logs and join the workout_logs table to get the date
        res = supabase.table("set_logs") \
            .select("weight, reps, set_number, workout_logs(created_at)") \
            .eq("user_id", user_id) \
            .eq("exercise_id", exercise_id) \
            .execute()
        return res.data
    except Exception as e:
        print(f"Error fetching exercise history: {e}")
        return []
