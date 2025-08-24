from openai import OpenAI
from app.config import AIMLAPI_KEY  # Updated to use a new config variable

# Initialize the OpenAI client with the aimlapi.com endpoint
client = OpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key=AIMLAPI_KEY,
)

def generate_affirmation(habit_name, status):
    """
    Calls GPT-4o via aimlapi.com to generate motivational messages.
    """
    if status == "Done":
        prompt = f"Give a short motivational message congratulating someone for completing the habit '{habit_name}' today."
    else:
        prompt = f"Give a short motivational message encouraging someone to try the habit '{habit_name}' tomorrow."

    try:
        response = client.chat.completions.create(
            model="openai/gpt-5-chat-latest",  # Using gpt-4o as specified
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2500,
        )
        message = response.choices[0].message.content.strip()
        return message
    except Exception as e:
        print(f"AI Error: {e}")  # Debug output
        return f"Keep going! Consistency with '{habit_name}' strengthens your brain."
