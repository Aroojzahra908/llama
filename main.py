# Replit Deployment Script for llama3.2-vision:11b
# Copy this to main.py in your Replit project

import subprocess
import time
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import threading
import os

# Install Ollama
def install_ollama():
    print("🚀 Installing Ollama...")
    subprocess.run(["curl", "-fsSL", "https://ollama.ai/install.sh", "-o", "install.sh"])
    subprocess.run(["bash", "install.sh"])
    print("✅ Ollama installed!")

# Install Ollama
install_ollama()

# Start Ollama in background
def start_ollama():
    subprocess.Popen(['ollama', 'serve'])

# Start Ollama
start_ollama()
time.sleep(10)

# Pull the llama3.2-vision:11b model
print("📥 Pulling llama3.2-vision:11b model...")
print("⏳ This may take 10-15 minutes...")
subprocess.run(['ollama', 'pull', 'llama3.2-vision:11b'])
print("✅ Model ready!")

# FastAPI App
app = FastAPI(
    title="Llama3.2 Vision API",
    description="A FastAPI service for llama3.2-vision:11b model",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model: str = "llama3.2-vision:11b"
    messages: list[ChatMessage]
    temperature: float = 0.7
    max_tokens: int = 1000

class GenerateRequest(BaseModel):
    model: str = "llama3.2-vision:11b"
    prompt: str
    temperature: float = 0.7
    max_tokens: int = 1000

@app.get("/")
async def root():
    return {
        "message": "Llama3.2 Vision API is running!",
        "model": "llama3.2-vision:11b",
        "status": "active",
        "endpoints": {
            "models": "/models",
            "chat": "/chat",
            "generate": "/generate",
            "health": "/health"
        }
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy", 
        "model": "llama3.2-vision:11b",
        "platform": "Replit"
    }

@app.get("/models")
async def list_models():
    """List available models"""
    return {
        "models": [
            {
                "name": "llama3.2-vision:11b",
                "size": "11B",
                "description": "Meta's Llama 3.2 Vision model with 11B parameters",
                "capabilities": ["text", "vision", "image_analysis"]
            }
        ]
    }

@app.post("/chat")
async def chat(request: ChatRequest):
    """Chat with llama3.2-vision:11b"""
    try:
        # Prepare messages for Ollama
        messages = [{"role": msg.role, "content": msg.content} for msg in request.messages]
        
        # Create prompt
        prompt = ""
        for msg in messages:
            if msg["role"] == "user":
                prompt += f"Human: {msg['content']}\n"
            elif msg["role"] == "assistant":
                prompt += f"Assistant: {msg['content']}\n"
        prompt += "Assistant:"
        
        # Call Ollama
        cmd = ["ollama", "run", request.model, prompt]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            response_text = result.stdout.strip()
            return {
                "response": response_text,
                "model": request.model,
                "status": "success",
                "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ")
            }
        else:
            raise HTTPException(status_code=500, detail=result.stderr)
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate")
async def generate(request: GenerateRequest):
    """Generate text using llama3.2-vision:11b"""
    try:
        # Call Ollama
        cmd = ["ollama", "run", request.model, request.prompt]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            response_text = result.stdout.strip()
            return {
                "response": response_text,
                "model": request.model,
                "status": "success",
                "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ")
            }
        else:
            raise HTTPException(status_code=500, detail=result.stderr)
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Start the API server
if __name__ == "__main__":
    print("🚀 Starting Llama3.2 Vision API on Replit...")
    print("📱 Your API will be available at the Replit public URL")
    print("🔗 Model: llama3.2-vision:11b")
    uvicorn.run(app, host="0.0.0.0", port=8000)
