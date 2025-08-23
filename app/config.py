import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

DB_URL = "sqlite:////mount/src/neuroscience_based_ai_habbit_tracker/habit_tracker.db"
AIMLAPI_KEY = os.getenv("AIMLAPI_KEY")
