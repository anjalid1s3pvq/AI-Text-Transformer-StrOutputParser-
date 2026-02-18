"""
Interactive CLI for AI Text Transformer

Allows users to input their own text for transformation.
"""

from ai_text_transformer import transform_text
import sys


def interactive_mode():
    """Run the application in interactive mode."""
    print("\n" + "=" * 80)
    print("AI TEXT TRANSFORMER - INTERACTIVE MODE")
    print("=" * 80)
    print("\nEnter a paragraph to transform (press Enter twice when done):")
    print("-" * 80)
    
    lines = []
    empty_line_count = 0
    
    while True:
        try:
            line = input()
            if line == "":
                empty_line_count += 1
                if empty_line_count >= 2:
                    break
            else:
                empty_line_count = 0
                lines.append(line)
        except EOFError:
            break
    
    text = " ".join(lines)
    
    if not text.strip():
        print("\nNo text provided. Exiting.")
        return
    
    print("\n-" * 40)
    print("Processing your text...\n")
    
    try:
        result = transform_text(text)
        print("TRANSFORMATION RESULTS:")
        print("=" * 80)
        print(result)
        print("=" * 80)
    except Exception as e:
        error_msg = str(e)
        print(f"\nError during transformation: {error_msg}\n")
        
        # Provide specific error guidance
        if "401" in error_msg or "invalid_api_key" in error_msg:
            print("❌ API Key Error: The OPENAI_API_KEY in your .env file is invalid or missing.")
            print("   Please check: https://platform.openai.com/account/api-keys")
        elif "429" in error_msg or "insufficient_quota" in error_msg:
            print("❌ Quota Error: Your OpenAI account has exceeded its usage quota.")
            print("   Please check your billing: https://platform.openai.com/account/billing/overview")
        elif "RateLimitError" in error_msg:
            print("❌ Rate Limit Error: Too many requests. Please wait a moment and try again.")
        else:
            print("⚠️  Make sure you have:")
            print("   1. Set OPENAI_API_KEY in your .env file")
            print("   2. Valid API key from https://platform.openai.com/account/api-keys")
            print("   3. Sufficient quota in your OpenAI account")


if __name__ == "__main__":
    interactive_mode()
