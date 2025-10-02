# 🚀 Deploy Llama3.2 Vision API (100% FREE)

## Quick Deployment on Replit

### Step 1: Create Replit Account
1. Go to [replit.com](https://replit.com)
2. Sign up with GitHub
3. Click "Create Repl" → "Python"

### Step 2: Deploy the API
1. **Delete the default `main.py`**
2. **Copy the content from `replit_deploy.py`**
3. **Paste it into `main.py`**
4. **Click "Run"**

### Step 3: Wait for Setup
- ⏳ Ollama installation: 2-3 minutes
- ⏳ Model download: 10-15 minutes
- ✅ API ready!

## 🌐 Your API is Live!

**Base URL:** `https://your-repl-name.your-username.repl.co`

### Test Your API

#### Health Check
```bash
curl https://your-repl-name.your-username.repl.co/health
```

#### Chat with Vision Model
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

#### Generate Text
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

## 📱 API Endpoints

- **GET /** - API information
- **GET /health** - Health check
- **GET /models** - List available models
- **POST /chat** - Chat with the model
- **POST /generate** - Generate text

## 🔧 Features

- ✅ **100% FREE** on Replit
- ✅ **llama3.2-vision:11b** model
- ✅ **Vision capabilities** for image analysis
- ✅ **REST API** for easy integration
- ✅ **CORS enabled** for web apps
- ✅ **Auto-restart** if it goes down

## 🎯 Use Cases

- Image analysis and description
- Computer vision applications
- AI-powered chatbots
- Content generation
- Educational tools

## 💡 Tips

1. **Keep Replit tab open** to prevent sleep
2. **Model loads on first request** (may take 30-60 seconds)
3. **Share your Replit URL** for public access
4. **Check logs** if something goes wrong

## 🆘 Troubleshooting

### Model not loading?
- Wait 5-10 minutes after first run
- Check Replit logs for errors
- Restart the Repl if needed

### API not responding?
- Make sure Replit is running
- Check the console for errors
- Try the health endpoint first

## 🎉 Success!

Your llama3.2-vision:11b API is now live and accessible to everyone! 🚀
