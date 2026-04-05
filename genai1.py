from dotenv import load_dotenv
load_dotenv()
import os
from google import genai
api_key=os.getenv("API_KEY")
client=genai.Client(api_key=api_key)
response=client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="how AI will change the education system in next 10years?",
)
print(response.text)






