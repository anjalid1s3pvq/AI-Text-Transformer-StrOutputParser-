"""
Example usage patterns for the AI Text Transformer
"""

from ai_text_transformer import transform_text


def example_1_technical_text():
    """Example 1: Transform technical documentation"""
    text = """
    The HTTP request-response protocol operates over TCP/IP and establishes a connection 
    on port 80 or 443 for encrypted communication. The client initiates by sending a request 
    line with method, URI, and version, followed by headers and optional body. The server 
    responds with a status line, response headers, and body containing the requested resource 
    or error information. Connection management can be persistent or non-persistent based on 
    the Connection header value.
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 1: TECHNICAL TEXT TRANSFORMATION")
    print("=" * 80)
    print("\nInput:")
    print(text.strip())
    print("\n" + "-" * 80)
    print(transform_text(text))


def example_2_casual_text():
    """Example 2: Transform casual writing"""
    text = """
    So like, I went to this amazing coffee shop yesterday, right? And the vibes were just 
    totally different from other places I've been to. The barista was super friendly and 
    made me this killer latte with some cool latte art on top. The whole place had these 
    chill indie songs playing in the background, and everyone was just doing their own thing 
    on their laptops or hanging out with friends. It's definitely becoming my new favorite spot!
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 2: CASUAL TEXT TRANSFORMATION")
    print("=" * 80)
    print("\nInput:")
    print(text.strip())
    print("\n" + "-" * 80)
    print(transform_text(text))


def example_3_formal_text():
    """Example 3: Transform formal business text"""
    text = """
    We hereby announce the implementation of new corporate policies regarding remote work 
    arrangements and flexible scheduling options. Effective immediately, all eligible employees 
    are authorized to work from designated locations outside the primary office facility, 
    subject to approval from their respective department heads. This initiative reflects our 
    organization's commitment to fostering work-life balance and enhancing employee satisfaction 
    whilst maintaining operational excellence and productivity standards.
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 3: FORMAL TEXT TRANSFORMATION")
    print("=" * 80)
    print("\nInput:")
    print(text.strip())
    print("\n" + "-" * 80)
    print(transform_text(text))


if __name__ == "__main__":
    try:
        example_1_technical_text()
        example_2_casual_text()
        example_3_formal_text()
    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure you have:")
        print("1. Installed dependencies: pip install -r requirements.txt")
        print("2. Set OPENAI_API_KEY in your .env file")
