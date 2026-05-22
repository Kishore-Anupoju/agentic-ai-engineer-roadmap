from google import genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)


def ask_agent(user_input):

    prompt = f"""
Convert this user request into ONLY a mathematical expression.

Examples:
User: what is 5 plus 5
Output: 5 + 5

User: multiply 10 by 8
Output: 10 * 8

User: what is 25 multiplied by 8 plus 10
Output: (25 * 8) + 10

Now convert:
{user_input}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()