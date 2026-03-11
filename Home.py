import streamlit as st
import random
from datetime import date
import os
import json

side= st.sidebar
side.title(':books: :gray[*StudyFlow*]')
side.divider()
side.caption('2026',text_alignment='center')


st.set_page_config(page_title="StudyFlow", layout="wide")

#for Json data
def get_task_stats():
    if os.path.exists("todo_data.json"):
        with open("todo_data.json", "r") as f:
            todos = json.load(f)
            total = len(todos)
            active = len([t for t in todos if not t["done"]])
            return total, active
    return 0, 0

def get_deadline_count():
    if os.path.exists("calendar_data.json"):
        with open("calendar_data.json", "r") as f:
            deadlines = json.load(f)
            return len(deadlines)
    return 0

total_tasks, active_tasks = get_task_stats()
deadline_count = get_deadline_count()

# --- FUN DATA ---
quotes = [
    "“Believe you can and you're halfway there.” – Theodore Roosevelt",
    "“It always seems impossible until it's done.” – Nelson Mandela",
    "“Don’t stop until you’re proud.”",
    "“Focus on being productive instead of busy.”",
    "“Your passion is waiting for your courage to catch up.”"
]

breaks = [
    "🎧 Listen to your favorite song and dance!",
    "🚶 Take a 5-minute walk outside.",
    "💧 Drink a full glass of water.",
    "🧘 Do 2 minutes of deep breathing.",
    "🍎 Eat a healthy snack.",
    "🃏 Do a quick 1-minute stretch."
]

# --- MAIN UI ---
st.title(':books: Study*Flow*', text_alignment='center')
st.caption('Your All-In One Study Companion.', text_alignment='center')
st.divider()

# 2. MOTIVATION CARD
with st.container(border=True):
    st.markdown(f"### 💡 Quote for Today!")
    if "daily_quote" not in st.session_state:
        st.session_state.daily_quote = random.choice(quotes)
    st.info(st.session_state.daily_quote)

# 3. STATS COLUMNS
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.metric(label="Today's Date", value=date.today().strftime("%b %d"))
        

with col2:
    with st.container(border=True):
        st.metric(label="Tasks Pending", value=active_tasks, )
        

with col3:
    with st.container(border=True):
        # CHANGED: Now tracking Deadlines instead of Notes
        st.metric(label="Upcoming Deadlines", value=deadline_count)
        

st.divider()

# 4. THE "BRAIN BREAK" GENERATOR
st.subheader("Want a break? Take a rest!")
st.caption("Click the button below to get a random 5-minute de-stress activity.")

if st.button("✨ Give me a Break Idea!", use_container_width=True, type="secondary"):
    idea = random.choice(breaks)
    st.balloons() 
    st.success(f"**Your Break Task:** {idea}")

# 5. QUICK NAVIGATION TILES
st.divider()
st.caption("📂 Go To...")
nav_col1, nav_col2, nav_col3 = st.columns(3)

with nav_col1:
    if st.button(" Open Notes", use_container_width=True):
        st.switch_page("pages/2_Notes.py")
with nav_col2:
    if st.button("Check Tasks", use_container_width=True):
        st.switch_page("pages/3_To Do.py")
with nav_col3:
    if st.button("View Deadlines", use_container_width=True):
        st.switch_page("pages/4_Calendar.py")
