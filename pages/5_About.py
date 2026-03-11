import streamlit as st


st.set_page_config(
    page_title="StudyFlow",
)
side= st.sidebar
side.title(':books: :gray[*StudyFlow*]')
side.divider()
side.caption('2026',text_alignment='center')

# --- HEADER SECTION ---
st.title(':books: Study*Flow*', text_alignment='center')
st.caption('Your All-In-One Study Companion.', text_alignment='center')
st.divider()

# --- MISSION STATEMENT (Justified) ---
st.markdown(
    """
    <div style="text-align: justify; line-height: 1.6; font-size: 1.1em; background-color: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px;">
        Welcome to <b>StudyFlow</b>! This is your all-in-one study companion designed to help 
        you stay organized, motivated, and on top of your academic game. Whether you 
        need to jot down notes, manage your to-do list, or keep track of important 
        deadlines, StudyFlow has got you covered. Navigate through the tabs to 
        explore all the features and make the most out of your study sessions. 
    </div>
    """, 
    unsafe_allow_html=True
)
st.divider()
st.write("") # Whitespace

# --- USE CASE & TARGET USER ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Use-Case")
    st.write(
        "StudyFlow is an academic planner and notes application designed to help students "
        "stay organized and productive. It combines note-taking, task management, and "
        "deadline tracking in one streamlined interface, making it easier to manage "
        "schoolwork without juggling multiple apps."
    )

with col2:
    st.subheader("👤 Target User")
    st.write(
        "StudyFlow is built specifically for students who want to keep track of lectures, "
        "assignments, exams, and daily study goals in a single, accessible platform."
    )

st.divider()

# --- INPUTS & OUTPUTS ---
st.subheader("⚙️ How It Works")

tab1, tab2 = st.tabs(["📥 Inputs (Collected)", "📤 Outputs (Displayed)"])

with tab1:
    st.markdown("""
    - **Class Notes:** Captured during lectures or deep study sessions.
    - **Tasks:** To-do items set for the day or week with priority levels.
    - **Deadlines:** Assignment, project, and exam details including event names, dates, and precise times.
    """)

with tab2:
    st.markdown("""
    - **Notes Library:** Organized storage for easy review and search.
    - **Task List:** Clear view of priorities with progress indicators and a completion archive.
    - **Smart Calendar:** Visual countdowns of upcoming deadlines and activity reminders.
    - **Motivational Dashboard:** Real-time tracking of pending work and suggested "Brain Break" ideas.
    """)

st.divider()
st.caption("Study*Flow* | 2026", text_alignment="center")
