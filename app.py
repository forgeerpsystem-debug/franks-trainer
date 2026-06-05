import os
import streamlit as st
from src.db.core import supabase

# Configure the browser tab
st.set_page_config(page_title="Franks Trainer", page_icon="💪", layout="centered")

if "user" not in st.session_state:
    st.session_state.user = None

# ==========================================
# THE INVISIBLE GATEWAY
# ==========================================
if st.session_state.user is None:
    try:
        # Pull credentials securely from environment variables
        email = os.environ.get("MASTER_EMAIL")
        password = os.environ.get("MASTER_PASSWORD")
        
        if not email or not password:
            st.error("Missing MASTER_EMAIL or MASTER_PASSWORD in environment variables.")
            st.stop()
            
        res = supabase.auth.sign_in_with_password({"email": email, "password": password})
        st.session_state.user = res.user
    except Exception as e:
        st.error(f"Auto-login failed. Verify your credentials in Supabase. Error: {e}")
        st.stop()

# ==========================================
# THE MAIN APP (No Login Screen!)
# ==========================================
# Header
st.title("💪 Franks Trainer")

# Native Mobile Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📋 Plan", "📝 Log", "📊 Stats", "🥩 Macros", "🍗 Meals", "⚙️ Manage"])

with tab1:
    from src.components import program
    program.render()
    
with tab2:
    from src.components import log_workout
    log_workout.render(user_id=st.session_state.user.id)
    
with tab3:
    from src.components import dashboard
    dashboard.render(user_id=st.session_state.user.id)
    
with tab4:
    from src.components import macros
    macros.render(user_id=st.session_state.user.id)
    
with tab5:
    from src.components import meal_plan
    meal_plan.render()
    
with tab6:
    from src.components import manage
    manage.render()