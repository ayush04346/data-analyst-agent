from fastapi import FastAPI, UploadFile, File
from agent import process_question

app = FastAPI()

@app.post("/api/")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    response = await process_question(content.decode())
    return response
