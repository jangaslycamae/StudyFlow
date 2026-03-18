import streamlit as st
import json
import os
from datetime import datetime, date, time

st.set_page_config(
    page_title="StudyFlow",
)
side= st.sidebar
side.title(':books: :gray[*StudyFlow*]')
side.divider()
side.caption('2026',text_alignment='center')

# --- DATABASE LOGIC ---
CAL_FILE = "calendar_data.json"

def load_events():
    if os.path.exists(CAL_FILE):
        with open(CAL_FILE, "r") as f:
            return json.load(f)
    return []

def save_events(events):
    with open(CAL_FILE, "w") as f:
        json.dump(events, f)

# --- UI SETUP ---
st.title("🗓️ Calendar")
events = load_all_events = load_events()
st.divider()

# 1. ADD NEW EVENT WITH TIME
with st.container(border=True):
    st.subheader("📌 Pin a Deadline")
    #st.divider()
    
    # Row 1: Name and Type
    col_a, col_b = st.columns([2, 1])
    with col_a:
        event_name = st.text_input("Event Name", placeholder="e.g., Programming")
    with col_b:
        event_type = st.selectbox("Type", ["Exam", "Assignment", "Project", "Presentation"])
    
    # Row 2: Date and Time
    col_c, col_d = st.columns(2)
    with col_c:
        event_date = st.date_input("Date", value=date.today())
    with col_d:
        event_time = st.time_input("Time", value=time().replace(hour=11, minute=59)) # Default to end of day

    if st.button("Add to Calendar", use_container_width=True):
        if event_name:
            # Combine date and time into one string for storage
            combined_dt = datetime.combine(event_date, event_time)
            events.append({
                "name": event_name,
                "datetime": combined_dt.strftime("%Y-%m-%d %H:%M:%S"),
                "type": event_type
            })
            # Sort by the full date and time
            events.sort(key=lambda x: x['datetime'])
            save_events(events)
            st.success(f"Added {event_name}!")
            st.rerun()

st.divider()

# 2. THE COUNTDOWN TIMELINE
st.subheader(" Deadlines")

if not events:
    st.info("No deadlines set. Take a breath!")
else:
    now = datetime.now()
    
    for i, ev in enumerate(events):
        # Convert stored string back to a real datetime object
        target_dt = datetime.strptime(ev['datetime'], "%Y-%m-%d %H:%M:%S")
        time_diff = target_dt - now
        
        # Calculate breakdown
        days = time_diff.days
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        # Style based on urgency
        if time_diff.total_seconds() < 0:
            status_text = "⚠️ OVERDUE"
            color = "gray"
        elif days == 0 and hours < 12:
            status_text = f"🚨 URGENT: {hours}h {minutes}m left!"
            color = "red"
        else:
            status_text = f"🕒 {days}d {hours}h {minutes}m remaining"
            color = "blue"

        with st.container(border=True):
            c1, c2, c3 = st.columns([0.25, 0.55, 0.2])
            with c1:
                # Display the formatted date and time
                st.write(f"**{target_dt.strftime('%b %d, %Y')}**")
                st.caption(f"At {target_dt.strftime('%I:%M %p')}")
            with c2:
                st.markdown(f"**{ev['name']}**")
                st.markdown(f":{color}[{ev['type']} — {status_text}]")
            with c3:
                if st.button("Done", key=f"del_ev_{i}", width='stretch'):
                    events.pop(i)
                    save_events(events)
                    st.rerun()
