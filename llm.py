import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Initialize OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# This function sends the natural language question to the LLM and returns code as response
async def get_task_plan(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # ✅ Works for all users
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful data analyst assistant. "
                    "The user will provide a data analysis question in plain English. "
                    "You must return only a valid Python script that uses standard libraries like pandas, matplotlib, duckdb, and numpy. "
                    "The script should define a variable `result` with the answer (like a number or string), "
                    "and if a plot is included, it should save it to a BytesIO buffer and assign the base64 string to `image_base64`."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content
