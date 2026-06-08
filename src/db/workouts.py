from src.db.core import supabase

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

def get_full_history(user_id: str):
    """Fetch all sets for a user joined with the parent workout date and exercise name."""
    try:
        response = supabase.table("set_logs") \
            .select("weight, reps, set_number, exercises(name), workout_logs!inner(created_at)") \
            .eq("user_id", user_id) \
            .execute()
        return response.data
    except Exception as e:
        print(f"Error fetching full history: {e}")
        return []
