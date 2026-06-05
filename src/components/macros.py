import streamlit as st
from src.db.macros import save_macros, get_todays_macros

def render(user_id: str):
    st.header("Daily Nutrition")
    
    # 1. Display Today's Running Totals
    totals = get_todays_macros(user_id)
    
    st.write("🔥 **Today's Totals**")
    cols = st.columns(4)
    cols[0].metric("Pro", f"{totals['protein']}g")
    cols[1].metric("Carb", f"{totals['carbs']}g")
    cols[2].metric("Fat", f"{totals['fats']}g")
    cols[3].metric("Cals", f"{totals['calories']}")
    
    st.divider()
    
    # 2. Input Form
    st.write("🍽️ **Log a Meal**")
    meal_name = st.text_input("Meal Name", placeholder="e.g., Post-workout shake")
    
    col1, col2, col3 = st.columns(3)
    p = col1.number_input("Protein (g)", min_value=0, step=1)
    c = col2.number_input("Carbs (g)", min_value=0, step=1)
    f = col3.number_input("Fats (g)", min_value=0, step=1)
    
    # Auto-calculate calories if left at 0
    auto_cals = (p * 4) + (c * 4) + (f * 9)
    cals = st.number_input("Calories", min_value=0, step=10, value=auto_cals)
    
    if st.button("Save Macros", type="primary", use_container_width=True):
        if save_macros(user_id, meal_name, p, c, f, cals):
            st.success(f"Logged {meal_name}!")
            st.rerun() # Refresh the page to update totals
        else:
            st.error("Failed to save macros.")