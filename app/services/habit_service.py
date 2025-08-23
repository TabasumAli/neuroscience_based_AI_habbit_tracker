# from app.database.models import Habit
# from app.database.session import SessionLocal

# class HabitService:
#     def __init__(self):
#         self.session = SessionLocal()

#     def add_habit(self, habit_name):
#         habit = Habit(habit_name=habit_name)
#         self.session.add(habit)
#         self.session.commit()
#         return habit

#     def get_habits(self):
#         return self.session.query(Habit).all()

from app.database.models import Habit
from app.database.session import SessionLocal
import streamlit as st

class HabitService:
    def __init__(self):
        self.session = SessionLocal()

    def add_habit(self, habit_name, user_id):
        try:
            habit = Habit(habit_name=habit_name, user_id=user_id)
            self.session.add(habit)
            self.session.commit()
            self.session.refresh(habit)
            return habit
        except Exception as e:
            self.session.rollback()
            st.error(f"Error adding habit: {str(e)}")
            raise

    def get_habits(self, user_id):
        try:
            return self.session.query(Habit).filter(Habit.user_id == user_id).all()
        except Exception as e:
            st.error(f"Error fetching habits: {str(e)}")
            return []
