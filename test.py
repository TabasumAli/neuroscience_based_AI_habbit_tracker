import openai
from app.config import AIMLAPI_KEY

openai.api_key = AIMLAPI_KEY

# quick test
try:
    response = openai.Model.list()
    print("API key works!")
except Exception as e:
    print(e)
