import streamlit as st

# Weekly meal prep and macro targets
WEEKLY_PLAN = {
    "Monday": {
        "focus": "Heavy Prep Day",
        "meals": [
            {"name": "Breakfast", "food": "4 Whole Eggs, 2 slices sourdough toast, 1 cup berries.", "macros": "30P / 45C / 20F"},
            {"name": "Lunch", "food": "Leftover Sunday Smoked Chicken Thighs (200g), 1.5 cups jasmine rice, BBQ sauce.", "macros": "45P / 65C / 15F"},
            {"name": "Pre-Workout", "food": "1 Banana, 1 scoop Whey Protein in water.", "macros": "25P / 27C / 2F"},
            {"name": "Dinner", "food": "Smoked Picanha (250g), roasted sweet potatoes, asparagus.", "macros": "60P / 50C / 40F"},
            {"name": "Snack", "food": "Greek Yogurt (1 cup) with honey.", "macros": "20P / 20C / 5F"}
        ]
    },
    "Tuesday": {
        "focus": "Quick & Efficient",
        "meals": [
            {"name": "Breakfast", "food": "Oatmeal (1 cup dry) cooked with whole milk, 1 scoop whey protein, peanut butter.", "macros": "40P / 65C / 20F"},
            {"name": "Lunch", "food": "Smoked Picanha slices (200g) in 2 flour tortillas, salsa, 1/2 avocado.", "macros": "45P / 50C / 35F"},
            {"name": "Pre-Workout", "food": "Rice Krispies Treat & Black Coffee.", "macros": "1P / 20C / 2F"},
            {"name": "Dinner", "food": "Lean Ground Beef (200g, 90/10), 1.5 cups pasta, marinara sauce.", "macros": "50P / 75C / 20F"},
            {"name": "Snack", "food": "Cottage Cheese (1 cup) or Protein Shake.", "macros": "25P / 10C / 5F"}
        ]
    },
    "Wednesday": {
        "focus": "Rest / Active Recovery",
        "meals": [
            {"name": "Breakfast", "food": "4 Whole Eggs, 1 cup spinach, 1/2 cup shredded cheese scramble.", "macros": "35P / 5C / 25F"},
            {"name": "Lunch", "food": "Smoked Chicken (200g), quinoa (1 cup), roasted peppers.", "macros": "50P / 40C / 10F"},
            {"name": "Dinner", "food": "Grilled Salmon (200g), 1 cup white rice, broccoli.", "macros": "45P / 45C / 25F"},
            {"name": "Snack", "food": "Protein Shake, 1 apple, handful of almonds.", "macros": "30P / 25C / 15F"}
        ]
    },
    "Thursday": {
        "focus": "Heavy Pull Fuel",
        "meals": [
            {"name": "Breakfast", "food": "3 Eggs, 2 packets instant oatmeal.", "macros": "25P / 55C / 15F"},
            {"name": "Lunch", "food": "Tuna salad (2 cans) with light mayo, whole wheat crackers.", "macros": "45P / 35C / 15F"},
            {"name": "Pre-Workout", "food": "1 Bagel with jam.", "macros": "10P / 50C / 2F"},
            {"name": "Dinner", "food": "Sirloin Steak (250g), massive baked potato, butter.", "macros": "55P / 60C / 25F"},
            {"name": "Snack", "food": "Whey Protein Shake.", "macros": "25P / 5C / 2F"}
        ]
    },
    "Friday": {
        "focus": "Arm Day / Pre-Weekend",
        "meals": [
            {"name": "Breakfast", "food": "Greek Yogurt (1.5 cups), granola, berries.", "macros": "30P / 60C / 8F"},
            {"name": "Lunch", "food": "Leftover Steak/Beef from Thursday, 1 cup rice.", "macros": "45P / 45C / 20F"},
            {"name": "Dinner", "food": "Homemade Burgers (2 patties, brioche buns), baked fries.", "macros": "55P / 70C / 35F"},
            {"name": "Snack", "food": "Optional based on hunger.", "macros": "-"}
        ]
    },
    "Saturday": {
        "focus": "Mountain Bike / Long Ride Fuel",
        "meals": [
            {"name": "Breakfast", "food": "Massive pancake stack (4 pancakes), maple syrup, 3 eggs.", "macros": "30P / 100C / 20F"},
            {"name": "Trail Snacks", "food": "Gummy bears, gels, or electrolyte carbs during ride.", "macros": "0P / 60C / 0F"},
            {"name": "Late Lunch", "food": "Chipotle Double Chicken Bowl (Rice, beans, cheese, guacamole).", "macros": "65P / 80C / 40F"},
            {"name": "Dinner", "food": "Big Green Egg Ribs (weekend smoke), coleslaw.", "macros": "40P / 20C / 35F"}
        ]
    },
    "Sunday": {
        "focus": "Smoke Day / Meal Prep",
        "meals": [
            {"name": "Breakfast", "food": "Bacon (4 slices), 3 Eggs, toast.", "macros": "30P / 30C / 30F"},
            {"name": "Lunch", "food": "Leftover Ribs or BBQ from Saturday.", "macros": "35P / 20C / 25F"},
            {"name": "Dinner", "food": "Fresh off the smoker: Chicken or Picanha, baked beans, cornbread.", "macros": "50P / 60C / 20F"},
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
    
    # Render mobile-friendly expanding menus for each day
    for day, data in WEEKLY_PLAN.items():
        with st.expander(f"📅 **{day}** - *{data['focus']}*"):
            for meal in data["meals"]:
                st.markdown(f"**{meal['name']}**")
                st.markdown(f"🥩 *{meal['food']}*")
                st.markdown(f"📊 `{meal['macros']}`")
                st.divider()