from src.db.core import supabase

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
