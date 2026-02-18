"""
AI Text Transformer using StrOutputParser

This module implements a text transformation pipeline that:
1. Summarizes input text (3-4 lines)
2. Detects the tone (Formal/Casual/Technical)
3. Provides an improved version of the text

Uses LangChain with Groq API for fast inference and StrOutputParser for clean string output.
Free API - no billing required!
"""

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def create_text_transformer():
    """
    Create and configure the text transformation pipeline.
    
    Returns:
        The configured chain (llm + prompt + parser)
    """
    
    # Initialize the language model using Groq (Free API)
    # Sign up at https://console.groq.com/keys
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",  # Works with your API key
        temperature=0.7,
        api_key=os.getenv("GROQ_API_KEY")
    )
    
    # Create the prompt template
    prompt_template = PromptTemplate(
        input_variables=["text"],
        template="""You are an expert text analyzer and refiner. Analyze the following paragraph and provide:

1. SUMMARY: Provide a concise summary in 3-4 lines
2. TONE: Identify the tone as one of: Formal, Casual, or Technical
3. IMPROVED VERSION: Provide an enhanced version of the text with better clarity, grammar, and flow

Text to analyze:
{text}

Format your response exactly as follows (use these headers):
SUMMARY:
[Your summary here]

TONE:
[Formal/Casual/Technical]

IMPROVED VERSION:
[Your improved text here]"""
    )
    
    # Create the output parser
    parser = StrOutputParser()
    
    # Chain the components: prompt -> model -> parser
    chain = prompt_template | llm | parser
    
    return chain


def transform_text(text: str) -> str:
    """
    Transform input text using the configured pipeline.
    
    Args:
        text (str): The paragraph to transform
        
    Returns:
        str: The transformation results as a plain string
    """
    chain = create_text_transformer()
    result = chain.invoke({"text": text})
    return result


def main():
    """Main function to demonstrate the text transformer."""
    
    # Example input text
    sample_text = """
    The rapid development of artificial intelligence technologies has revolutionized various industries.
    Machine learning algorithms can now process vast amounts of data and identify patterns that humans 
    might miss. Companies are increasingly investing in AI research to gain competitive advantages.
    However, concerns about job displacement and ethical implications continue to grow.
    """
    
    print("=" * 80)
    print("AI TEXT TRANSFORMER - DEMONSTRATION")
    print("=" * 80)
    print("\nInput Text:")
    print("-" * 80)
    print(sample_text.strip())
    print("-" * 80)
    
    print("\nProcessing...\n")
    
    try:
        # Transform the text
        result = transform_text(sample_text)
        
        print("Transformation Results:")
        print("=" * 80)
        print(result)
        print("=" * 80)
    except Exception as e:
        error_msg = str(e)
        print("❌ Error during transformation:\n")
        print(error_msg)
        print("\n" + "=" * 80)
        print("Troubleshooting:")
        print("=" * 80)
        
        if "401" in error_msg or "invalid_api_key" in error_msg:
            print("❌ API Key Error: The OPENAI_API_KEY is invalid or missing.")
            print("   → Check your .env file")
            print("   → Get a new key: https://platform.openai.com/account/api-keys")
        elif "429" in error_msg or "insufficient_quota" in error_msg:
            print("❌ Quota Error: Your OpenAI account has insufficient quota.")
            print("   → Check billing: https://platform.openai.com/account/billing/overview")
            print("   → Add payment method or upgrade your plan")
        elif "RateLimitError" in error_msg:
            print("❌ Rate Limit: Too many requests in a short time.")
            print("   → Please wait a moment and try again")
        else:
            print("⚠️  Ensure you have:")
            print("   1. Valid OPENAI_API_KEY in .env file")
            print("   2. Sufficient quota in your OpenAI account")
            print("   3. Internet connection to OpenAI API")


if __name__ == "__main__":
    main()
