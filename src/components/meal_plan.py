import streamlit as st
import json
import os
from src.config import MACROS

@st.cache_data
def load_meals_data():
    file_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "meals.json")
    with open(file_path, "r") as f:
        return json.load(f)

def render():
    st.header("🍗 Fuel Plan")
    
    st.write("🔥 **Daily Baseline Target:**")
    cols = st.columns(4)
    cols[0].metric("Cals", f"{MACROS['calories']:,}")
    cols[1].metric("Pro", f"{MACROS['protein']}g")
    cols[2].metric("Carb", f"{MACROS['carbs']}g")
    cols[3].metric("Fat", f"{MACROS['fats']}g")
    
    st.divider()
    st.write("👉 *Tap a day to expand meals*")
    
    weekly_plan = load_meals_data()
    
    for day, data in weekly_plan.items():
        with st.expander(f"📅 **{day}** - *{data['focus']}*"):
            for meal in data["meals"]:
                st.markdown(f"**{meal['name']}**")
                st.markdown(f"🥩 *{meal['food']}*")
                st.markdown(f"📊 `{meal['macros']}`")
                st.divider()
