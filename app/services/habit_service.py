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

class HabitService:
    def __init__(self):
        self.session = SessionLocal()

    def add_habit(self, habit_name, user_id):
        habit = Habit(habit_name=habit_name, user_id=user_id)
        self.session.add(habit)
        self.session.commit()
        return habit

    def get_habits(self, user_id):
        return self.session.query(Habit).filter(Habit.user_id == user_id).all()
