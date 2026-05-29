import streamlit as st

# Your specific Anatoly Powerbuilding Split pre-loaded with target weights
ANATOLY_SPLIT = {
    "Day 1: Squat & Lower Body": [
        {"name": "Back Squat", "sets": "5", "reps": "8, 5, 5, 3-5, 3", "target": "72.5kg ➔ 102.5kg", "notes": "Primary pyramid. 3 min rest before Set 4 and 5. Explosive drive out of the hole."},
        {"name": "Front Squat", "sets": "4", "reps": "6-8", "target": "Moderate", "notes": "Keep it light, focus on upright torso and deep range of motion."},
        {"name": "Leg Press", "sets": "3", "reps": "8-10", "target": "Heavy", "notes": "Final set to failure."},
        {"name": "Romanian Deadlift", "sets": "3", "reps": "8-10", "target": "Moderate", "notes": "Strict hamstring stretch. Squeeze glutes at top."}
    ],
    "Day 2: Bench Press & Push": [
        {"name": "Bench Press", "sets": "5", "reps": "8, 5, 5, 3-5, 3", "target": "55kg ➔ 77.5kg", "notes": "Primary pyramid. 3 min rest on heavy sets. Leg drive and tight lats on the unrack."},
        {"name": "Incline Dumbbell Press", "sets": "4", "reps": "6-8", "target": "Heavy", "notes": "Upper chest focus. Deep stretch at the bottom."},
        {"name": "Dumbbell Flyes", "sets": "3", "reps": "10-12", "target": "Light", "notes": "Strict form, focus on the stretch, no ego lifting."},
        {"name": "Tricep Dips", "sets": "4", "reps": "To Failure", "target": "Bodyweight+", "notes": "Add weight if you are hitting more than 15 reps."}
    ],
    "Day 3: Deadlift & Pull": [
        {"name": "Conventional Deadlift", "sets": "5", "reps": "8, 5, 5, 3-5, 3", "target": "85kg ➔ 120kg", "notes": "Primary pyramid. Pull the slack out of the bar before driving the floor away. 3 min rest for Set 5."},
        {"name": "Barbell Row", "sets": "4", "reps": "6-8", "target": "Heavy", "notes": "Heavy mid-back thickness. Keep torso parallel to the floor."},
        {"name": "Weighted Pull-Ups", "sets": "4", "reps": "To Failure", "target": "Bodyweight+", "notes": "Strict form, no kipping. Full extension at the bottom."},
        {"name": "Face Pulls", "sets": "3", "reps": "15-20", "target": "Light", "notes": "Rear delt and rotator cuff health. Squeeze for a second at the top."}
    ],
    "Day 4: Overhead Press & Arms": [
        {"name": "Overhead Press", "sets": "5", "reps": "8, 5, 5, 3-5, 3", "target": "35kg ➔ 55kg", "notes": "Primary pyramid. Squeeze glutes and brace core hard before pressing to protect the spine."},
        {"name": "Dumbbell Lateral Raises", "sets": "4", "reps": "12-15", "target": "Moderate", "notes": "Slow and controlled. No swinging from the hips."},
        {"name": "Barbell Curl", "sets": "3", "reps": "8-10", "target": "Heavy", "notes": "Bicep strength. Keep elbows pinned to your sides."},
        {"name": "Hammer Curl", "sets": "3", "reps": "10-12", "target": "Moderate", "notes": "Brachialis development for arm thickness."}
    ]
}

def render():
    st.header("📋 The Plan")
    
    # Dropdown to select the current day
    day_selected = st.selectbox("Select Training Day", options=list(ANATOLY_SPLIT.keys()), label_visibility="collapsed")
    
    st.divider()
    
    # Fetch the specific workout data for the selected day
    exercises = ANATOLY_SPLIT[day_selected]
    
    # Render mobile-friendly cards for each movement
    for ex in exercises:
        with st.container(border=True):
            st.subheader(ex["name"])
            
            # Use columns to stack metrics cleanly on a phone
            cols = st.columns(3)
            cols[0].metric("Sets", ex["sets"])
            cols[1].metric("Reps", ex["reps"])
            cols[2].metric("Target", ex["target"])
            
            # App note for form and execution
            st.info(f"💡 **Note:** {ex['notes']}")