# AI Text Transformer using StrOutputParser

Build a text transformation pipeline using a local language model (Ollama), custom prompts, and StrOutputParser.

## 📋 Project Overview

This application implements a text transformation pipeline that:
1. **Summarizes** input text into 3-4 lines
2. **Detects the tone** (Formal, Casual, or Technical)
3. **Improves** the paragraph with better clarity, grammar, and flow

All output is returned as **plain strings** (not JSON) using LangChain's `StrOutputParser`.

## ✨ Key Features

- 🚀 **Runs Locally** - Uses Ollama for 100% local LLM inference
- 🔐 **No API Keys** - Completely private, no internet required
- 💰 **Free** - No costs, use as much as you want
- 📦 **Multiple Models** - Switch between Mistral, Neural-Chat, Llama2, etc.
- ✅ **PromptTemplate** for structured text analysis
- ✅ **StrOutputParser** for clean string output formatting
- ✅ **Chain Pattern** (Prompt → Model → Parser)
- ✅ **LangChain Integration** with Ollama

## 🎯 Quick Start

### Prerequisites
- **Ollama** installed on your system (you already have this!)
- Python 3.8+

### Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start Ollama:**
   ```bash
   ollama serve
   ```
   (Keep this running in a separate terminal)

3. **Download a model:**
   ```bash
   ollama pull mistral
   ```

4. **Run the application:**
   ```bash
   python ai_text_transformer.py
   ```

## 📖 Full Setup Guide

See [OLLAMA_SETUP.md](OLLAMA_SETUP.md) for:
- Detailed Ollama configuration
- Available models and performance comparison
- Troubleshooting guide
- System requirements

## 🎮 Usage

### Run the Demo
```bash
python ai_text_transformer.py
```

This runs the application with a pre-defined sample text to demonstrate the transformation.

### Interactive Mode
```bash
python interactive_cli.py
```

Enter your own paragraph and the system will analyze and transform it.

### Programmatic Usage
```python
from ai_text_transformer import transform_text

text = "Your paragraph here..."
result = transform_text(text)
print(result)
```

## 📄 Output Format

The output is structured as plain text with clear sections:

```
SUMMARY:
[3-4 line summary of the text]

TONE:
[Formal/Casual/Technical]

IMPROVED VERSION:
[Enhanced version of the original text]
```

## 🏗️ Architecture

The application uses the **LangChain Chain Pattern**:

```
Input Text
    ↓
PromptTemplate (formats the prompt with input)
    ↓
Ollama LLM (processes with local model)
    ↓
StrOutputParser (converts output to plain string)
    ↓
Output (plain string result)
```

## 📝 Implementation Details

### Key Components

1. **Language Model** (Ollama): Local LLM inference
   - Model: Mistral (default, easily changeable)
   - Temperature: 0.7 (balanced creativity)
   - No API key required!

2. **PromptTemplate**: Structures the analysis request
   - Defines input variables
   - Sets the exact format for output
   - Ensures consistent results

3. **StrOutputParser**: Returns plain string output
   - No JSON parsing required
   - Direct string results
   - Clean and simple output

### Chain Setup

```python
llm = Ollama(model="mistral", temperature=0.7)
chain = prompt_template | llm | parser
result = chain.invoke({"text": input_text})
```

## 🔧 Changing Models

To use a different model, edit `ai_text_transformer.py`:

```python
llm = Ollama(
    model="neural-chat",  # or llama2, orca-mini, phi, etc.
    temperature=0.7,
    base_url="http://localhost:11434"
)
```

### Recommended Models

| Model | Speed | Quality | Size | Download |
|-------|-------|---------|------|----------|
| **mistral** | ⚡⚡ | ⭐⭐⭐⭐ | 4GB | `ollama pull mistral` |
| neural-chat | ⚡⚡ | ⭐⭐⭐ | 4GB | `ollama pull neural-chat` |
| llama2 | ⚡ | ⭐⭐⭐⭐⭐ | 7GB | `ollama pull llama2` |
| orca-mini | ⚡⚡⚡ | ⭐⭐ | 1.3GB | `ollama pull orca-mini` |
| phi | ⚡⚡⚡ | ⭐⭐ | 1.6GB | `ollama pull phi` |

## 📚 Files Structure

```
.
├── ai_text_transformer.py    # Main application logic
├── interactive_cli.py         # Interactive user interface
├── examples.py               # Usage examples
├── requirements.txt          # Python dependencies
├── .env.example             # (Optional config)
├── OLLAMA_SETUP.md          # Detailed Ollama guide
└── README.md                # This file
```

## ✅ Evaluation Criteria - Implementation

- ✅ **Correct Model Usage**: Ollama with temperature control
- ✅ **Proper Prompt Engineering**: Well-structured PromptTemplate with clear instructions
- ✅ **Clean Chaining Structure**: Uses the pipe operator for readable chains
- ✅ **Correct StrOutputParser Usage**: Returns plain strings, not JSON
- ✅ **Output Format**: Plain text with organized sections (no JSON)

## 🚀 Advantages Over OpenAI

| Aspect | Ollama (Local) | OpenAI (API) |
|--------|---|---|
| Cost | **Free** | Pay per token |
| Privacy | **100% Private** | Data sent to API |
| API Keys | **Not needed** | Required |
| Quotas | **Unlimited** | Limited by plan |
| Speed | **Fast** (local) | Network dependent |
| Internet | **Not required** | Required |
| Models | **Multiple** | Limited selection |

## 📖 References

- [Ollama Official](https://ollama.ai)
- [LangChain Documentation](https://python.langchain.com)
- [Available Ollama Models](https://ollama.ai/library)
- [PromptTemplate](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/)
- [Output Parsers](https://python.langchain.com/docs/modules/model_io/output_parsers/)

## 🐛 Troubleshooting

**Q: "Failed to connect to Ollama"**  
A: Make sure `ollama serve` is running in another terminal

**Q: "Model not found"**  
A: Download it first: `ollama pull mistral`

**Q: Application is slow**  
A: Use a smaller model like orca-mini or phi

See [OLLAMA_SETUP.md](OLLAMA_SETUP.md) for more troubleshooting tips.

## 📄 License

MIT License - feel free to use and modify

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests or open issues.

## 🎮 Usage

### Run the Demo
```bash
python ai_text_transformer.py
```

This runs the application with a pre-defined sample text to demonstrate the transformation.

### Interactive Mode
```bash
python interactive_cli.py
```

Enter your own paragraph and the system will analyze and transform it.

### Programmatic Usage
```python
from ai_text_transformer import transform_text

text = "Your paragraph here..."
result = transform_text(text)
print(result)
```

## 📄 Output Format

The output is structured as plain text with clear sections:

```
SUMMARY:
[3-4 line summary of the text]

TONE:
[Formal/Casual/Technical]

IMPROVED VERSION:
[Enhanced version of the original text]
```

## 🏗️ Architecture

The application uses the **LangChain Chain Pattern**:

```
Input Text
    ↓
PromptTemplate (formats the prompt with input)
    ↓
ChatOpenAI (processes with GPT model)
    ↓
StrOutputParser (converts output to plain string)
    ↓
Output (plain string result)
```

## 📝 Implementation Details

### Key Components

1. **Language Model** (`ChatOpenAI`): Powers the text analysis
   - Model: GPT-3.5-turbo
   - Temperature: 0.7 (balanced creativity)

2. **PromptTemplate**: Structures the analysis request
   - Defines input variables
   - Sets the exact format for output
   - Ensures consistent results

3. **StrOutputParser**: Returns plain string output
   - No JSON parsing required
   - Direct string results
   - Clean and simple output

### Chain Setup

```python
chain = prompt_template | llm | parser
result = chain.invoke({"text": input_text})
```

## 🔐 Environment Variables

Create a `.env` file with:
```
OPENAI_API_KEY=your_api_key_here
```

Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)

## 🧪 Testing

Run the demo script:
```bash
python ai_text_transformer.py
```

Expected output should show:
- A 3-4 line summary
- Identified tone (Formal, Casual, or Technical)
- An improved version of the input text

## 📚 Files Structure

```
.
├── ai_text_transformer.py    # Main application logic
├── interactive_cli.py         # Interactive user interface
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
└── README.md                 # This file
```

## ✅ Evaluation Criteria - Implementation

- ✅ **Correct Model Usage**: ChatOpenAI with temperature control
- ✅ **Proper Prompt Engineering**: Well-structured PromptTemplate with clear instructions
- ✅ **Clean Chaining Structure**: Uses the pipe operator for readable chains
- ✅ **Correct StrOutputParser Usage**: Returns plain strings, not JSON
- ✅ **Output Format**: Plain text with organized sections (no JSON)

## 🔧 Customization

### Change the Model
Edit `ai_text_transformer.py` and modify the model parameter:
```python
llm = ChatOpenAI(model="gpt-4", temperature=0.5)
```

### Customize the Prompt
Modify the `template` parameter in `PromptTemplate` to change analysis behavior.

### Adjust Temperature
Change `temperature` (0-1) to control creativity levels:
- 0: Deterministic
- 0.7: Balanced (default)
- 1: Maximum creativity

## 📖 References

- [LangChain Documentation](https://python.langchain.com)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [PromptTemplate](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/)
- [Output Parsers](https://python.langchain.com/docs/modules/model_io/output_parsers/)

## 📄 License

MIT License - feel free to use and modify
