# Llama3.2 Vision API

A FastAPI service that provides HTTP access to the llama3.2-vision:11b model, making it available for public use.

## Features

- 🚀 FastAPI-based REST API
- 🤖 llama3.2-vision:11b model (11B parameters)
- 👁️ Vision capabilities for image analysis
- 💬 Chat completion endpoints
- 📝 Text generation endpoints
- 🌐 CORS enabled for web access
- 🆓 100% FREE deployment on Replit

## API Endpoints

### Core Endpoints

- `GET /` - API information and available endpoints
- `GET /health` - Health check and Ollama connection status
- `GET /models` - List available Ollama models

### Model Interaction

- `POST /chat` - Chat with a model using conversation format
- `POST /generate` - Generate text from a prompt
- `POST /pull` - Pull a model from Ollama registry

## 🚀 Quick Deployment (100% FREE)

### Deploy on Replit

1. **Go to [replit.com](https://replit.com)**
2. **Sign up with GitHub**
3. **Create new Python Repl**
4. **Copy content from `replit_deploy.py`**
5. **Paste into `main.py`**
6. **Click "Run"**
7. **Wait 10-15 minutes for model download**
8. **Your API is live!** 🎉

### Local Development

1. **Install Ollama**:
   ```bash
   # Download from https://ollama.ai
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Pull the vision model**:
   ```bash
   ollama pull llama3.2-vision:11b
   ```

4. **Run the API**:
   ```bash
   python main.py
   ```

5. **Access the API**:
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs

## API Usage Examples

### Chat with Vision Model

```bash
curl -X POST "https://your-repl-name.your-username.repl.co/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.2-vision:11b",
    "messages": [
      {"role": "user", "content": "Hello! Tell me about computer vision."}
    ],
    "temperature": 0.7,
    "max_tokens": 500
  }'
```

### Generate Text

```bash
curl -X POST "https://your-repl-name.your-username.repl.co/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.2-vision:11b",
    "prompt": "Explain how computer vision works",
    "temperature": 0.8,
    "max_tokens": 1000
  }'
```

### Health Check

```bash
curl -X GET "https://your-repl-name.your-username.repl.co/health"
```

## 🎯 Model Capabilities

The llama3.2-vision:11b model supports:
- **Text generation** and conversation
- **Image analysis** and description
- **Computer vision** tasks
- **Multimodal** understanding
- **Code generation** and analysis

## 🔧 Configuration

### Model Details
- **Model**: llama3.2-vision:11b
- **Parameters**: 11 billion
- **Capabilities**: Text + Vision
- **Size**: ~6.5GB

### API Settings
- **Default temperature**: 0.7
- **Max tokens**: 1000
- **CORS**: Enabled for all origins
- **Timeout**: 120 seconds

## 🆘 Troubleshooting

### Common Issues

1. **Model not loading**: Wait 10-15 minutes after first deployment
2. **API timeout**: Check Replit logs for errors
3. **Slow responses**: Normal for first request (model loading)

### Health Check

```bash
curl https://your-repl-name.your-username.repl.co/health
```

## 🎉 Success!

Your llama3.2-vision:11b API is now live and accessible to everyone! 🚀

## License

MIT License - feel free to use this for your projects!

