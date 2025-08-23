import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

DB_URL = "sqlite:////tmp/habit_tracker.db"
AIMLAPI_KEY = os.getenv("AIMLAPI_KEY")
