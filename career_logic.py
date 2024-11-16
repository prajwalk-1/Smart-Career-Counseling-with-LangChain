from langchain.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI LLM
llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key, model_name="gpt-3.5-turbo")

def career_chat(input_text):
    """
    Provides career advice based on user input.
    """
    prompt = f"You are a career coach. {input_text}"
    return llm(prompt)

def generate_mock_interview(industry):
    """
    Simulates a mock interview based on the industry.
    """
    prompt = f"Generate a mock interview for the {industry} industry. Include 5 questions and sample answers."
    return llm(prompt)
