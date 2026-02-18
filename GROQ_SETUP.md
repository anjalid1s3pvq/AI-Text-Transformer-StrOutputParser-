# Groq Setup Guide

Switch from OpenAI to **Groq** - a completely FREE API with no billing issues!

## 🎉 Why Groq?

✅ **100% Free** - No billing, no credit card needed  
✅ **Super Fast** - Blazing fast inference (often faster than OpenAI)  
✅ **Generous Free Tier** - Unlimited requests (fair usage)  
✅ **No Quotas** - Use it as much as you want  
✅ **Easy Setup** - Takes 2 minutes  
✅ **Multiple Models** - Mixtral, Llama 2, etc.  

## 📋 Quick Setup (3 Steps)

### Step 1: Create a Groq Account
1. Go to **https://console.groq.com/keys**
2. Click "Sign Up" (completely free)
3. Fill in your details
4. Verify your email

### Step 2: Get Your API Key
1. After signing up, you'll be on the **API Keys** page
2. Click "Create New API Key" or copy the default key
3. Copy the entire key (looks like: `gsk_XXXXXXXXXXXX...`)

### Step 3: Set Up Your .env File
In the terminal, run:
```bash
echo 'GROQ_API_KEY=paste_your_key_here' > .env
```

Replace `paste_your_key_here` with your actual API key.

**Example:**
```bash
echo 'GROQ_API_KEY=gsk_wVaBDf1Tr5KJ2mD3xYzQ' > .env
```

## ✅ Verify Setup

Run this to test:
```bash
python -c "from ai_text_transformer import transform_text; print('✅ Ready to go!')"
```

## 🚀 Run Your App

```bash
# Demo mode
python ai_text_transformer.py

# Interactive mode
python interactive_cli.py

# Examples
python examples.py
```

## 📊 Available Groq Models

| Model | Speed | Quality | Best For |
|-------|-------|---------|----------|
| **mixtral-8x7b-32768** | ⚡⚡⚡ Fast | ⭐⭐⭐⭐ Excellent | **Recommended** |
| llama2-70b-4096 | ⚡⚡ Medium | ⭐⭐⭐⭐⭐ Best | Elaborate tasks |
| gemma-7b-it | ⚡⚡⚡ Fast | ⭐⭐⭐ Good | Quick tasks |

### Change Model (Optional)

Edit `ai_text_transformer.py`, line ~28:
```python
llm = ChatGroq(
    model="llama2-70b-4096",  # Change model here
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)
```

## 🔍 Troubleshooting

### Error: "Invalid API Key"
- Check you copied the entire key (including `gsk_` prefix)
- Make sure it's in the `.env` file: `cat .env`
- Try getting a new key from https://console.groq.com/keys

### Error: "Module not found"
```bash
pip install -q langchain-groq
```

### Slow Response
- This is normal for first request (cold start)
- Groq is actually faster than OpenAI
- Try a smaller model if still slow

### Rate Limit (429 Error)
- You hit the fair usage limit
- Wait a few minutes
- Groq free tier is very generous - this rarely happens

## 💰 Groq Pricing

**FREE FOREVER** for reasonable usage
- No daily limits
- No monthly limits
- Fair usage policy applies
- Upgrade to pro if you need massive scale (unusual)

## 🎯 Performance Comparison

| Aspect | Groq | OpenAI |
|--------|------|--------|
| Speed | ⚡⚡⚡ Fastest | ⚡⚡ Medium |
| Cost | **FREE** | Pay per token |
| Setup | Very easy | Requires card |
| Reliability | Excellent | Excellent |
| Models | Multiple | Limited free |

## ✨ Next Steps

1. ✅ Sign up at https://console.groq.com/keys
2. ✅ Copy your API key
3. ✅ Create `.env` file: `echo 'GROQ_API_KEY=your_key' > .env`
4. ✅ Run: `python ai_text_transformer.py`

## 🔗 Resources

- **Groq Console:** https://console.groq.com/keys
- **Groq Documentation:** https://console.groq.com/docs
- **LangChain Groq Integration:** https://python.langchain.com/docs/integrations/providers/groq

---

**You're all set!** Your AI Text Transformer now uses the fastest free LLM API available. 🚀
