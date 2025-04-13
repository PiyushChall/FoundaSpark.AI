import os
import google.generativeai as genai

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the model
model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_idea_with_ai(idea: str) -> str:
    prompt = f"""
    Analyze the following startup idea in detail and return:
    - Uniqueness
    - Market potential
    - Feasibility
    - Target audience
    - Risk factors

    Startup Idea: "{idea}"
    """
    response = model.generate_content(prompt)
    return response.text
