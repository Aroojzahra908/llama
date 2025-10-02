from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import json
from typing import Optional, List
import uvicorn

app = FastAPI(
    title="Llama3.2 Vision API",
    description="A FastAPI service for llama3.2-vision:11b model",
    version="1.0.0"
)

# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
OLLAMA_BASE_URL = "http://localhost:11434"  # Default Ollama URL

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    stream: Optional[bool] = False
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1000

class GenerateRequest(BaseModel):
    model: str
    prompt: str
    stream: Optional[bool] = False
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1000

class ModelInfo(BaseModel):
    name: str
    size: int
    digest: str
    modified_at: str

@app.get("/")
async def root():
    return {
        "message": "Llama3.2 Vision API is running!",
        "model": "llama3.2-vision:11b",
        "endpoints": {
            "models": "/models",
            "chat": "/chat",
            "generate": "/generate",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    """Check if Ollama service is running"""
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        if response.status_code == 200:
            return {"status": "healthy", "ollama_connected": True}
        else:
            return {"status": "unhealthy", "ollama_connected": False}
    except requests.exceptions.RequestException:
        return {"status": "unhealthy", "ollama_connected": False}

@app.get("/models")
async def list_models():
    """List available Ollama models"""
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags")
        if response.status_code == 200:
            models = response.json().get("models", [])
            return {"models": models}
        else:
            raise HTTPException(status_code=500, detail="Failed to fetch models")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Ollama service unavailable: {str(e)}")

@app.post("/chat")
async def chat(request: ChatRequest):
    """Chat with an Ollama model"""
    try:
        payload = {
            "model": request.model,
            "messages": [{"role": msg.role, "content": msg.content} for msg in request.messages],
            "stream": request.stream,
            "options": {
                "temperature": request.temperature,
                "num_predict": request.max_tokens
            }
        }
        
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/chat",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            # Return a clean chatbot response
            return {
                "response": data.get("message", {}).get("content", ""),
                "model": data.get("model", request.model),
                "created_at": data.get("created_at", ""),
                "done": data.get("done", True)
            }
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
            
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Ollama service unavailable: {str(e)}")

@app.post("/generate")
async def generate(request: GenerateRequest):
    """Generate text using an Ollama model"""
    try:
        payload = {
            "model": request.model,
            "prompt": request.prompt,
            "stream": request.stream,
            "options": {
                "temperature": request.temperature,
                "num_predict": request.max_tokens
            }
        }
        
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            # Return a clean response for text generation
            return {
                "response": data.get("response", ""),
                "model": data.get("model", request.model),
                "created_at": data.get("created_at", ""),
                "done": data.get("done", True)
            }
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
            
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Ollama service unavailable: {str(e)}")

@app.post("/pull")
async def pull_model(model_name: str):
    """Pull a model from Ollama registry"""
    try:
        payload = {"name": model_name}
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/pull",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            return {"message": f"Model {model_name} pulled successfully"}
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
            
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Ollama service unavailable: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

