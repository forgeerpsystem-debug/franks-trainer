import streamlit as st

# Weekly meal prep and macro targets (5:40 AM Training / Whole Foods Only)
WEEKLY_PLAN = {
    "Monday": {
        "focus": "Heavy Squat Fuel",
        "meals": [
            {"name": "5:00 AM (Pre-Workout)", "food": "CJC-1295 (fasted). 1 Banana, Black Coffee, 5g Creatine.", "macros": "1P / 27C / 0F"},
            {"name": "7:15 AM (Post-Workout)", "food": "4 Whole Eggs, 1 cup Greek Yogurt, 2 slices sourdough toast.", "macros": "45P / 45C / 20F"},
            {"name": "12:00 PM (Lunch)", "food": "Leftover Sunday Smoked Chicken Thighs (200g), 1.5 cups jasmine rice.", "macros": "45P / 65C / 15F"},
            {"name": "6:00 PM (Dinner)", "food": "Smoked Picanha (250g), roasted sweet potatoes, asparagus.", "macros": "60P / 50C / 40F"},
            {"name": "8:00 PM (Snack)", "food": "Cottage Cheese (1 cup) with honey.", "macros": "25P / 20C / 5F"}
        ]
    },
    "Tuesday": {
        "focus": "Heavy Bench Fuel",
        "meals": [
            {"name": "5:00 AM (Pre-Workout)", "food": "CJC-1295. Rice Krispies Treat, Black Coffee, 5g Creatine.", "macros": "1P / 22C / 2F"},
            {"name": "7:15 AM (Post-Workout)", "food": "Oatmeal (1 cup dry) cooked with whole milk, side of 1 cup Cottage Cheese.", "macros": "35P / 65C / 15F"},
            {"name": "12:00 PM (Lunch)", "food": "Smoked Picanha slices (200g) in 2 flour tortillas, salsa, 1/2 avocado.", "macros": "45P / 50C / 35F"},
            {"name": "6:00 PM (Dinner)", "food": "Lean Ground Beef (200g, 90/10), 1.5 cups pasta, marinara sauce.", "macros": "50P / 75C / 20F"},
            {"name": "8:00 PM (Snack)", "food": "Greek Yogurt (1 cup).", "macros": "20P / 8C / 0F"}
        ]
    },
    "Wednesday": {
        "focus": "Rest / Active Recovery",
        "meals": [
            {"name": "6:00 AM (Wake)", "food": "CJC-1295 (fasted). Black Coffee.", "macros": "0P / 0C / 0F"},
            {"name": "8:00 AM (Breakfast)", "food": "4 Whole Eggs, 1 cup spinach, 1/2 cup shredded cheese scramble.", "macros": "35P / 5C / 25F"},
            {"name": "12:00 PM (Lunch)", "food": "Smoked Chicken (200g), quinoa (1 cup), roasted peppers.", "macros": "50P / 40C / 10F"},
            {"name": "6:00 PM (Dinner)", "food": "Grilled Salmon (200g), 1 cup white rice, broccoli.", "macros": "45P / 45C / 25F"},
            {"name": "8:00 PM (Snack)", "food": "Cottage cheese (1 cup), 1 apple, handful of almonds.", "macros": "30P / 25C / 15F"}
        ]
    },
    "Thursday": {
        "focus": "Heavy Deadlift Fuel",
        "meals": [
            {"name": "5:00 AM (Pre-Workout)", "food": "CJC-1295. 1 Bagel with jam, Black Coffee, 5g Creatine.", "macros": "10P / 50C / 2F"},
            {"name": "7:15 AM (Post-Workout)", "food": "3 Eggs, 2 packets instant oatmeal.", "macros": "25P / 55C / 15F"},
            {"name": "12:00 PM (Lunch)", "food": "Tuna salad (2 cans) with light mayo, whole wheat crackers.", "macros": "45P / 35C / 15F"},
            {"name": "6:00 PM (Dinner)", "food": "Sirloin Steak (250g), massive baked potato, butter.", "macros": "55P / 60C / 25F"},
            {"name": "8:00 PM (Snack)", "food": "Greek Yogurt (1 cup).", "macros": "20P / 8C / 0F"}
        ]
    },
    "Friday": {
        "focus": "Overhead & Arms",
        "meals": [
            {"name": "5:00 AM (Pre-Workout)", "food": "CJC-1295. 1 Banana, Black Coffee, 5g Creatine.", "macros": "1P / 27C / 0F"},
            {"name": "7:15 AM (Post-Workout)", "food": "Greek Yogurt (1.5 cups), large handful of granola, berries.", "macros": "30P / 60C / 8F"},
            {"name": "12:00 PM (Lunch)", "food": "Leftover Steak/Beef from Thursday, 1 cup rice.", "macros": "45P / 45C / 20F"},
            {"name": "6:00 PM (Dinner)", "food": "Homemade Burgers (2 patties, brioche buns), baked fries.", "macros": "55P / 70C / 35F"},
            {"name": "8:00 PM (Snack)", "food": "Optional based on hunger.", "macros": "-"}
        ]
    },
    "Saturday": {
        "focus": "Mountain Bike Fuel",
        "meals": [
            {"name": "7:00 AM (Pre-Ride)", "food": "CJC-1295. Massive pancake stack (4 pancakes), maple syrup, 3 eggs.", "macros": "30P / 100C / 20F"},
            {"name": "Trail Snacks", "food": "Gummy bears, gels, or electrolyte carbs during ride.", "macros": "0P / 60C / 0F"},
            {"name": "2:00 PM (Late Lunch)", "food": "Chipotle Double Chicken Bowl (Rice, beans, cheese, guacamole).", "macros": "65P / 80C / 40F"},
            {"name": "7:00 PM (Dinner)", "food": "Big Green Egg Ribs (weekend smoke), coleslaw.", "macros": "40P / 20C / 35F"}
        ]
    },
    "Sunday": {
        "focus": "Smoke Day / Meal Prep",
        "meals": [
            {"name": "8:00 AM (Breakfast)", "food": "CJC-1295. Bacon (4 slices), 3 Eggs, toast.", "macros": "30P / 30C / 30F"},
            {"name": "1:00 PM (Lunch)", "food": "Leftover Ribs or BBQ from Saturday.", "macros": "35P / 20C / 25F"},
            {"name": "6:00 PM (Dinner)", "food": "Fresh off the smoker: Chicken or Picanha, baked beans.", "macros": "50P / 60C / 20F"},
            {"name": "Prep", "food": "Smoke 2kg of chicken thighs and a roast for Monday/Tuesday lunches.", "macros": "Prep"}
        ]
    }
}

def render():
    st.header("🍗 Fuel Plan")
    
    st.write("🔥 **Daily Baseline Target:**")
    cols = st.columns(4)
    cols[0].metric("Cals", "2,850")
    cols[1].metric("Pro", "180g")
    cols[2].metric("Carb", "300g")
    cols[3].metric("Fat", "95g")
    
    st.divider()
    st.write("👉 *Tap a day to expand meals*")
    
    for day, data in WEEKLY_PLAN.items():
        with st.expander(f"📅 **{day}** - *{data['focus']}*"):
            for meal in data["meals"]:
                st.markdown(f"**{meal['name']}**")
                st.markdown(f"🥩 *{meal['food']}*")
                st.markdown(f"📊 `{meal['macros']}`")
                st.divider()