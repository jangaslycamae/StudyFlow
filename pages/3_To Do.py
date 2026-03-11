import streamlit as st
import json
import os

st.set_page_config(
    page_title="StudyFlow",
)
side= st.sidebar
side.title(':books: :gray[*StudyFlow*]')
side.divider()
side.caption('2026',text_alignment='center')

# --- DATABASE LOGIC ---
TODO_FILE = "todo_data.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f)

# --- UI SETUP ---
st.title("📝 To Do's")
st.divider()

todos = load_todos()

# 1. TOP SECTION: ADD NEW TASK
with st.container(border=True):
    st.subheader("🟨 New Task ")
    st.divider()
    col1, col2 = st.columns([3, 1])
    
    with col1:
        new_task = st.text_input("What needs to be done?", placeholder="e.g., Study for Chem Quiz")
    with col2:
        priority = st.selectbox("Priority", ["High", "Medium", "Low"])
    
    if st.button("Add to List", use_container_width=True):
        if new_task.strip():
            todos.append({"task": new_task, "priority": priority, "done": False})
            save_todos(todos)
            st.rerun()
        else:
            st.warning("Please enter a task name!")

st.divider()

# 2. PROGRESS BAR
if todos:
    completed_list = [t for t in todos if t["done"]]
    active_list = [t for t in todos if not t["done"]]
    
    total = len(todos)
    progress = len(completed_list) / total if total > 0 else 0
    
    st.write(f"**Overall Progress:** {len(completed_list)}/{total} tasks done")
    st.progress(progress)
else:
    active_list = []
    completed_list = []

# 3. MIDDLE SECTION: ACTIVE TASKS
st.subheader("Tasks")
if not active_list:
    st.info("whoo! No active tasks. Enjoy your free time! 🎉")
else:
    for i, item in enumerate(todos):
        if not item["done"]:
            # Logic to find the right emoji for priority
            color = "🟥" if item["priority"] == "High" else "🟨" if item["priority"] == "Medium" else "🟦"
            
            with st.container(border=True):
                c1, c2, c3 = st.columns([0.1, 0.75, 0.15])
                with c1:
                    if st.checkbox("Done", key=f"chk_{i}", label_visibility="collapsed"):
                        todos[i]["done"] = True
                        save_todos(todos)
                        st.rerun()
                with c2:
                    st.write(f"{color} **{item['task']}**")
                with c3:
                    if st.button("⨉",type='primary', width='stretch', key=f"del_{i}"):
                        todos.pop(i)
                        save_todos(todos)
                        st.rerun()

st.divider()

# 4. BOTTOM SECTION: COMPLETED TASKS
st.subheader("Finished Tasks")
if not completed_list:
    st.caption("Completed tasks will appear here.")
else:
    for i, item in enumerate(todos):
        if item["done"]:
            # A more subtle look for finished items
            c1, c2 = st.columns([0.85, 0.15])
            with c1:
                st.write(f"✅ ~~{item['task']}~~ ")
            with c2:
                if st.button("Undo", key=f"undo_{i}"):
                    todos[i]["done"] = False
                    save_todos(todos)
                    st.rerun()
