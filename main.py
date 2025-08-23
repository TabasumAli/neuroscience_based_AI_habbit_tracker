# import streamlit as st
# from app.database.models import Base
# from app.database.session import engine
# from app.services.habit_service import HabitService
# from app.services.log_service import LogService
# from app.services.ai_service import generate_affirmation
# from app.utils.viz import plot_habits

# # Create tables
# Base.metadata.create_all(engine)

# st.title("🧠 Neuroscience-Informed Habit Tracker")

# habit_service = HabitService()
# log_service = LogService()

# # --- Add Habit ---
# st.subheader("Add a New Habit")
# habit_name = st.text_input("Habit Name")
# if st.button("Add Habit"):
#     if habit_name.strip():
#         habit_service.add_habit(habit_name.strip())
#         st.success(f"Habit '{habit_name}' added!")

# # --- Fetch Habits ---
# habits = habit_service.get_habits()

# # --- Log Today's Habits ---
# st.subheader("Log Today's Habits")
# if habits:
#     habits_per_page = 5
#     total_pages = (len(habits) + habits_per_page - 1) // habits_per_page
#     current_page = st.session_state.get("page", 1)

#     start_idx = (current_page - 1) * habits_per_page
#     end_idx = start_idx + habits_per_page
#     paginated_habits = habits[start_idx:end_idx]

#     for habit in paginated_habits:
#         st.write(f"**{habit.habit_name}** (Current Streak: {habit.streak} days)")
#         status = st.radio(f"{habit.habit_name}", ["Done", "Skip"], key=habit.id)
#         if st.button(f"Log {habit.habit_name}", key=f"log-{habit.id}"):
#             message = generate_affirmation(habit.habit_name, status)
#             log_service.log_habit(habit.id, status, message)
#             st.info(message)

#     # Pagination controls
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col1:
#         if st.button("Previous", key="prev", disabled=current_page == 1):
#             st.session_state.page = max(1, current_page - 1)
#     with col2:
#         st.write(f"Page {current_page} of {total_pages}")
#     with col3:
#         if st.button("Next", key="next", disabled=current_page == total_pages):
#             st.session_state.page = min(total_pages, current_page + 1)
# else:
#     st.write("No habits yet. Add a habit above to start tracking!")

# # --- Progress Dashboard ---
# st.subheader("Progress Dashboard")
# logs = log_service.get_logs()
# if logs:
#     st.plotly_chart(plot_habits(logs))
# else:
#     st.write("No logs yet. Start logging your habits to see progress!")

# # --- Clear All Data ---
# st.subheader("Clear All Data")
# if st.button("Clear All Data"):
#     if st.session_state.get("confirm_clear", False):
#         log_service.clear_all_data()
#         st.session_state.confirm_clear = False
#         st.success("All habits and logs have been cleared!")
#     else:
#         st.warning("Are you sure? Click again to confirm clearing all habits and logs.")

import streamlit as st
from app.database.base import Base
from app.database.session import engine, SessionLocal
from app.services.habit_service import HabitService
from app.services.log_service import LogService
from app.services.ai_service import generate_affirmation
from app.utils.viz import plot_habits
import uuid
from sqlalchemy import inspect

# Initialize session state
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())
if 'db_initialized' not in st.session_state:
    # Check if tables exist before creating
    inspector = inspect(engine)
    required_tables = {'habits', 'habit_logs', 'ai_insights'}
    existing_tables = set(inspector.get_table_names())
    if not required_tables.issubset(existing_tables):
        Base.metadata.create_all(engine)
    st.session_state.db_initialized = True

# Display user_id for demo purposes (optional)
st.write(f"User ID: {st.session_state.user_id}")

st.title("🧠 Neuroscience-Informed Habit Tracker")

habit_service = HabitService()
log_service = LogService()

# --- Add Habit ---
st.subheader("Add a New Habit")
habit_name = st.text_input("Habit Name", key="habit_input")
if st.button("Add Habit"):
    if habit_name.strip():
        habit_service.add_habit(habit_name.strip(), st.session_state.user_id)
        st.session_state.habit_input = ""  # Clear input after adding
        st.success(f"Habit '{habit_name}' added!")

# --- Fetch Habits ---
habits = habit_service.get_habits(st.session_state.user_id)

# --- Log Today's Habits ---
st.subheader("Log Today's Habits")
if habits:
    habits_per_page = 5
    total_pages = (len(habits) + habits_per_page - 1) // habits_per_page
    current_page = st.session_state.get("page", 1)

    start_idx = (current_page - 1) * habits_per_page
    end_idx = start_idx + habits_per_page
    paginated_habits = habits[start_idx:end_idx]

    for habit in paginated_habits:
        st.write(f"**{habit.habit_name}** (Current Streak: {habit.streak} days)")
        status = st.radio(f"Status for {habit.habit_name}", ["Done", "Skip"], key=f"radio-{st.session_state.user_id}-{habit.id}")
        if st.button(f"Log {habit.habit_name}", key=f"log-{st.session_state.user_id}-{habit.id}"):
            message = generate_affirmation(habit.habit_name, status)
            log_service.log_habit(habit.id, status, message, st.session_state.user_id)
            st.info(message)

    # Pagination controls
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("Previous", key="prev", disabled=current_page == 1):
            st.session_state.page = max(1, current_page - 1)
    with col2:
        st.write(f"Page {current_page} of {total_pages}")
    with col3:
        if st.button("Next", key="next", disabled=current_page == total_pages):
            st.session_state.page = min(total_pages, current_page + 1)
else:
    st.write("No habits yet. Add a habit above to start tracking!")

# --- Progress Dashboard ---
st.subheader("Progress Dashboard")
logs = log_service.get_logs(st.session_state.user_id)
if logs:
    st.plotly_chart(plot_habits(logs))
else:
    st.write("No logs yet. Start logging your habits to see progress!")

# --- Clear All Data ---
st.subheader("Clear All Data")
if st.button("Clear All Data"):
    if st.session_state.get("confirm_clear", False):
        log_service.clear_all_data(st.session_state.user_id)
        st.session_state.confirm_clear = False
        st.success("All your habits and logs have been cleared!")
    else:
        st.warning("Are you sure? Click again to confirm clearing all your habits and logs.")
        st.session_state.confirm_clear = True
