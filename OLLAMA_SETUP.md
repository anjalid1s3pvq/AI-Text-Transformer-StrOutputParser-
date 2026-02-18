# Ollama Setup Guide

This application now uses **Ollama** for local LLM inference - no API keys required!

## ✅ You Already Have Ollama Installed!

Great! Follow these steps to get started:

## 📥 Step 1: Make Sure Ollama is Running

Open a terminal and start the Ollama server:

```bash
ollama serve
```

You should see output like:
```
time=2026-02-18T... level=INFO msg="Listening on 127.0.0.1:11434 (version ...)"
```

**Keep this terminal open while running the transformer.**

## 📦 Step 2: Download a Model

Open another terminal and choose a model to download:

### Recommended Models (Ranked by Speed & Quality):

1. **Mistral** (Best balance - recommended) - 4GB
   ```bash
   ollama pull mistral
   ```

2. **Neural Chat** (Good quality, fast) - 4GB
   ```bash
   ollama pull neural-chat
   ```

3. **Llama 2** (Largest, best quality) - 7GB+
   ```bash
   ollama pull llama2
   ```

4. **Orca Mini** (Smallest, fastest) - 1.3GB
   ```bash
   ollama pull orca-mini
   ```

5. **Phi** (Very small, good for laptops) - 1.6GB
   ```bash
   ollama pull phi
   ```

### Check Installed Models:
```bash
ollama list
```

## 🚀 Step 3: Run the Application

```bash
# Demo mode
python ai_text_transformer.py

# Interactive mode
python interactive_cli.py
```

## ⚙️ Step 4: (Optional) Change Model

Edit `ai_text_transformer.py` and change line 25:

```python
llm = Ollama(
    model="mistral",  # ← Change this to your model name
    temperature=0.7,
    base_url="http://localhost:11434"
)
```

Available models: `mistral`, `neural-chat`, `llama2`, `orca-mini`, `phi`, etc.

## 🎯 Performance Tips

| Model | Size | Speed | Quality | Use Case |
|-------|------|-------|---------|----------|
| orca-mini | 1.3GB | ⚡⚡⚡ Fast | ⭐⭐ Basic | Learning, testing |
| phi | 1.6GB | ⚡⚡⚡ Fast | ⭐⭐ Basic | Lightweight |
| neural-chat | 4GB | ⚡⚡ Medium | ⭐⭐⭐ Good | Balanced choice |
| mistral | 4GB | ⚡⚡ Medium | ⭐⭐⭐⭐ Excellent | **Recommended** |
| llama2 | 7-13GB | ⚡ Slow | ⭐⭐⭐⭐⭐ Best | High quality |

## 🔧 Troubleshooting

### Error: "Failed to connect to Ollama"
- Make sure you ran `ollama serve` in another terminal
- Check if server is on port 11434: Open http://localhost:11434 in browser
- On some systems, Ollama may be on a different URL

### Error: "Model not found"
- Download the model: `ollama pull mistral`
- Check installed models: `ollama list`

### Slow Performance
- Use a smaller model (orca-mini or phi)
- Close other applications
- Check system RAM usage

### Out of Memory
- Use a smaller model
- Close browser/heavy applications
- On GPU systems, ensure GPU is enabled

## 📊 System Requirements

| Model | RAM Needed | Disk Space |
|-------|-----------|-----------|
| orca-mini | 2GB+ | 2GB |
| phi | 2GB+ | 2GB |
| neural-chat | 4GB+ | 5GB |
| mistral | 4GB+ | 5GB |
| llama2 | 8GB+ | 15GB |

## 🌐 Custom Ollama Server

If Ollama is running on a different machine:

Edit `ai_text_transformer.py`:
```python
llm = Ollama(
    model="mistral",
    base_url="http://192.168.1.100:11434"  # Your Ollama server IP
)
```

## ✨ Benefits of Ollama

✅ **No API Keys** - Run completely local  
✅ **No Quotas** - Use as much as you want  
✅ **No Internet Required** - Full privacy  
✅ **No Costs** - Completely free  
✅ **Fast** - Runs on your GPU if available  
✅ **Easy to Switch Models** - Just pull a different one  

## 📚 More Information

- Ollama Website: https://ollama.ai
- Available Models: https://ollama.ai/library
- Documentation: https://github.com/ollama/ollama

Enjoy your local AI text transformer! 🎉
