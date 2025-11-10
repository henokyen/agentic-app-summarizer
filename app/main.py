from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
import os
from app.openai_client import summerize_text    
from app.schemas import SummarizeRequest, SummarizeResponse

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse('static/index.html')

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "text-summarization-api"}

@app.post("/summarize", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest):
    try:
        return StreamingResponse(
            summerize_text(request.text),
            media_type="text/plain")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))