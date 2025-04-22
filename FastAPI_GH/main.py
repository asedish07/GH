from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

IP = os.getenv("IP")
if not IP:
    raise HTTPException(status_code=500, detail="IP not set in environment variables")

app = FastAPI()

@app.get("/")
async def hello():
  return "Hello, World!"

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("main:app", host=IP, port=9070, reload=True)