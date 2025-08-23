from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime, date

Base = declarative_base()

class Habit(Base):
    __tablename__ = 'habits'
    id = Column(Integer, primary_key=True)
    habit_name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    streak = Column(Integer, default=0)  # New column for habit streak
    logs = relationship("HabitLog", back_populates="habit")

class HabitLog(Base):
    __tablename__ = 'habit_logs'
    id = Column(Integer, primary_key=True)
    habit_id = Column(Integer, ForeignKey('habits.id'))
    date = Column(Date, default=date.today)
    status = Column(String)
    habit = relationship("Habit", back_populates="logs")
    insights = relationship("AIInsight", back_populates="habit_log")

class AIInsight(Base):
    __tablename__ = 'ai_insights'
    id = Column(Integer, primary_key=True)
    habit_log_id = Column(Integer, ForeignKey('habit_logs.id'))
    message = Column(String)
    habit_log = relationship("HabitLog", back_populates="insights")

