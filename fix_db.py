
from sqlalchemy import create_engine, text
from app.config import DB_URL

# Connect to the database
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

# Add the streak column to the habits table
with engine.connect() as connection:
    connection.execute(text("ALTER TABLE habits ADD COLUMN streak INTEGER DEFAULT 0"))
    connection.commit()  # Ensure the change is committed
    print("Added streak column to habits table.")
