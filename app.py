import streamlit as st
from src.components import log_workout
from src.database import supabase

st.set_page_config(page_title="Franks Trainer", page_icon="💪", layout="centered")

# Ensure session state variables exist
if "user" not in st.session_state:
    st.session_state.user = None

# Mobile Gateway Screen
if st.session_state.user is None:
    st.title("💪 Franks Trainer")
    st.subheader("Mobile Access Gateway")
    
    email = st.text_input("Email", placeholder="your-email@example.com")
    password = st.text_input("Password", type="password", placeholder="••••••••")
    
    if st.button("Login", type="primary", use_container_width=True):
        try:
            res = supabase.auth.sign_in_with_password({"email": email, "password": password})
            st.session_state.user = res.user
            st.rerun()
        except Exception as e:
            st.error("Authentication failed. Check your credentials.")
else:
    # Header user bar
    cols = st.columns([3, 1])
    cols[0].title("💪 Franks Trainer")
    if cols[1].button("Exit", use_container_width=True):
        supabase.auth.sign_out()
        st.session_state.user = None
        st.rerun()
        
   # Native Mobile Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📝 Log", "📊 Stats", "🥩 Macros", "⚙️ Manage"])
    
    with tab1:
        log_workout.render(user_id=st.session_state.user.id)
        
    with tab2:
        from src.components import dashboard
        dashboard.render(user_id=st.session_state.user.id)
        
    with tab3:
        from src.components import macros
        macros.render(user_id=st.session_state.user.id)
        
    with tab4:
        from src.components import manage
        manage.render()