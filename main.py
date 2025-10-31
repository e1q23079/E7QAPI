# main.py
import os
import json

from dotenv import load_dotenv
import uvicorn

from fastapi import FastAPI

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
APIKEY = os.getenv('APIKEY')

# Initialize FastAPI app
app = FastAPI(docs_url="/documentation",title="E7QAPI", version="1.0.0", description="API for e7qAPI status codes",summary="e7qAPI")

# Load data from JSON file
data = json.load(open('data/data.json', 'r', encoding='utf-8'))

# Define routes

# Root endpoint
@app.get("/")
async def read_root():
    return {"mes": "e7qAPI is running!"}

# Test endpoint
@app.get("/test/{text}")
async def test(text:str):
    return {"text": text}

# Status endpoint
@app.get("/status",tags=["status"])
async def status(code:str = None,api_key:str = None):
    if api_key != APIKEY:
        return {"status": "Invalid API Key."}
    try:
        status = data[code]
    except KeyError:
        status = "Code not found."   
    return {"status": status}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)