import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Missing Supabase credentials in .env file")

# Initialize the single client instance
supabase: Client = create_client(url, key)

def get_exercises():
    """Fetch the master list of exercises for the dropdowns."""
    try:
        response = supabase.table("exercises").select("*").execute()
        return response.data
    except Exception as e:
        print(f"Error fetching exercises: {e}")
        return []

def save_workout(user_id: str, exercise_id: str, sets_data: list, notes: str):
    """Inserts a workout log and all associated sets into Postgres."""
    try:
        # 1. Insert parent workout log
        workout_res = supabase.table("workout_logs").insert({
            "user_id": user_id,
            "notes": notes
        }).execute()
        
        if not workout_res.data:
            return False, "Failed to initialize workout log."
            
        workout_id = workout_res.data[0]["id"]
        
        # 2. Prepare bulk payload for sets
        set_payload = []
        for row in sets_data:
            # Skip empty or unconfigured rows
            if row.get("Weight (kg)") is None or row.get("Reps") is None:
                continue
            if row["Weight (kg)"] == 0 and row["Reps"] == 0:
                continue
                
            set_payload.append({
                "workout_log_id": workout_id,
                "user_id": user_id,
                "exercise_id": exercise_id,
                "set_number": int(row["Set"]),
                "weight": float(row["Weight (kg)"]),
                "reps": int(row["Reps"])
            })
            
        if not set_payload:
            return False, "No valid sets to save."
            
        # 3. Bulk insert sets
        supabase.table("set_logs").insert(set_payload).execute()
        return True, "Workout saved successfully! 💪"
        
    except Exception as e:
        return False, f"Database error: {str(e)}"    

def get_workout_history(user_id: str):
    """Fetch all sets for a user joined with the parent workout date."""
    try:
        response = supabase.table("set_logs") \
            .select("weight, reps, workout_logs(created_at)") \
            .eq("user_id", user_id) \
            .execute()
        return response.data
    except Exception as e:
        print(f"Error fetching history: {e}")
        return []
    
def save_macros(user_id: str, meal_name: str, p: int, c: int, f: int, cals: int):
    """Inserts a new macro log."""
    try:
        supabase.table("macro_logs").insert({
            "user_id": user_id,
            "meal_name": meal_name,
            "protein": p,
            "carbs": c,
            "fats": f,
            "calories": cals
        }).execute()
        return True
    except Exception as e:
        print(f"Error saving macros: {e}")
        return False

def get_todays_macros(user_id: str):
    """Fetches today's macros and sums them up."""
    from datetime import datetime
    today = datetime.now().date().isoformat()
    
    try:
        res = supabase.table("macro_logs") \
            .select("protein, carbs, fats, calories") \
            .eq("user_id", user_id) \
            .eq("log_date", today) \
            .execute()
            
        data = res.data
        if not data:
            return {"protein": 0, "carbs": 0, "fats": 0, "calories": 0}
            
        # Sum up the columns
        return {
            "protein": sum(item['protein'] for item in data),
            "carbs": sum(item['carbs'] for item in data),
            "fats": sum(item['fats'] for item in data),
            "calories": sum(item['calories'] for item in data),
        }
    except Exception as e:
        print(f"Error fetching macros: {e}")
        return {"protein": 0, "carbs": 0, "fats": 0, "calories": 0}
    
def add_exercise(name: str, category: str):
    """Inserts a new custom exercise into the library."""
    try:
        supabase.table("exercises").insert({
            "name": name,
            "category": category
        }).execute()
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