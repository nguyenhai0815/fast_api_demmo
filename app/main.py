from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
import time

app = FastAPI()

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str

@app.post("/stream")
async def stream_text(request: TextRequest):
    async def generate_text():
        words = request.text.split()
        for word in words:
            await time.sleep(2)
            yield word

    return StreamingResponse(generate_text(), media_type="text/plain")
