from fastapi import FastAPI, UploadFile, File
from agent import process_question
from dotenv import load_dotenv
import os

load_dotenv()  # reads .env in the project root
api_key = os.getenv("OPENAI_API_KEY")


app = FastAPI()

@app.post("/api/")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    response = await process_question(content.decode())
    return response
