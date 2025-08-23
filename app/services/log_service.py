from app.database.models import HabitLog, AIInsight, Habit
from app.database.session import SessionLocal
from datetime import date, timedelta

class LogService:
    def __init__(self):
        self.session = SessionLocal()

    def log_habit(self, habit_id, status, message=None):
        log = HabitLog(habit_id=habit_id, date=date.today(), status=status)
        self.session.add(log)
        self.session.commit()
        
        # Update habit streak
        habit = self.session.query(Habit).get(habit_id)
        yesterday = date.today() - timedelta(days=1)
        prev_log = self.session.query(HabitLog).filter(
            HabitLog.habit_id == habit_id,
            HabitLog.date == yesterday
        ).first()
        
        if status == "Done":
            if prev_log and prev_log.status == "Done":
                habit.streak = habit.streak + 1 if habit.streak else 1
            else:
                habit.streak = 1
        else:  # status == "Skip"
            habit.streak = 0
        self.session.commit()
        
        if message:
            insight = AIInsight(habit_log_id=log.id, message=message)
            self.session.add(insight)
            self.session.commit()
        return log

    def get_logs(self):
        return self.session.query(HabitLog).join(HabitLog.habit).all()

    def clear_all_data(self):
        self.session.query(AIInsight).delete()
        self.session.query(HabitLog).delete()
        self.session.query(Habit).delete()
        self.session.commit()