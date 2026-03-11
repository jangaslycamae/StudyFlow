import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="StudyFlow",
)
side= st.sidebar
side.title(':books: :gray[*StudyFlow*]')
side.divider()
side.caption('2026',text_alignment='center')


DB_FILE = "studyflow_data.json"

def load_all_notes():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_to_db(title, content):
    notes = load_all_notes()
    notes[title] = {
        "content": content,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    with open(DB_FILE, "w") as f:
        json.dump(notes, f)

if "edit_title" not in st.session_state:
    st.session_state["edit_title"] = ""
if "edit_content" not in st.session_state:
    st.session_state["edit_content"] = ""

# MAIN
st.title("📋 My Notes")
st.divider()

# THE EDITOR (TITLE & CONTENT)
note_title = st.text_input("Title", value=st.session_state["edit_title"], placeholder="Enter note title...")
note_content = st.text_area("Write your notes...", value=st.session_state["edit_content"], height=200)

col1, col2 = st.columns(2)

with col1:
    if st.button("Save Note", use_container_width=True, icon=":material/save:"):
        if note_title.strip() and note_content.strip():
            save_to_db(note_title, note_content)
            # CLEAR THE AREA after saving
            st.session_state["edit_title"] = ""
            st.session_state["edit_content"] = ""
            st.success("Saved! Area cleared.")
            st.rerun()
        else:
            st.error("Fill in both title and content!")

with col2:
    if st.button("Clear", use_container_width=True, icon=":material/mop:"):
        st.session_state["edit_title"] = ""
        st.session_state["edit_content"] = ""
        st.rerun()

st.divider()

# SEARCH BAR
saved_notes = load_all_notes()
search_query = st.text_input("Search your notes...", placeholder="Type a keyword to find a note", icon= ":material/search:")

st.subheader("📙 Your Library")

# Filter notes
if search_query:
    filtered_notes = {k: v for k, v in saved_notes.items() if search_query.lower() in k.lower() or search_query.lower() in v['content'].lower()}
else:
    filtered_notes = saved_notes

if not filtered_notes:
    st.info("No saved notes yet.")
else:
    for title, data in reversed(list(filtered_notes.items())):
        with st.expander(f"{title} — {data['date']}"):
            st.write(data['content'])
            st.divider()
            
            btn_col1, btn_col2 = st.columns(2)
            
            with btn_col1:
                if st.button(f" Edit", key=f"edit_{title}", icon=":material/edit:", width='stretch'):
                    st.session_state["edit_title"] = title
                    st.session_state["edit_content"] = data['content']
                    st.rerun()
            
            with btn_col2:
                if st.button(f"Delete", key=f"del_{title}", icon=":material/delete:",width='stretch', type='primary'):
                    del saved_notes[title]
                    with open(DB_FILE, "w") as f:
                        json.dump(saved_notes, f)
                    st.rerun()
