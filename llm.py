import os
import google.generativeai as genai
import json  # Use safe JSON parsing instead of eval

# Configure the API key
genai.configure(api_key="AIzaSyDkKktyTOTvNi_aBHYItxzUfyNukFBn6Vs")  # Use env var in production

# Load the model
model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_idea_with_ai(idea: str) -> dict:
    prompt = f"""
    You are a startup idea evaluation expert.

    Analyze the following startup idea and respond ONLY in a clean JSON object without explanation:

    Startup Idea: "{idea}"

    Return JSON with the following keys:
    - idea_length: number of words
    - is_unique: Yes or No
    - clarity_score: rate from 1 to 10
    - target_market_identified: Yes or No
    - problem_solution_fit: Weak/Moderate/Strong
    - feasibility_level: Low/Medium/High
    - revenue_potential: Low/Moderate/High
    - potential_for_growth: Low/Medium/High
    """

    print("Sending to LLM...")
    response = model.generate_content(prompt)
    raw_text = response.text.strip()
    '''print("Raw LLM response:", raw_text)'''

    try:
        # Extract JSON from possible markdown formatting
        if raw_text.startswith("```json"):
            raw_text = raw_text.lstrip("```json").rstrip("```").strip()

        result = json.loads(raw_text)
        return result
    except json.JSONDecodeError:
        print("Error parsing response:", raw_text)
        return {
            "idea_length": "N/A",
            "is_unique": "N/A",
            "clarity_score": "N/A",
            "target_market_identified": "N/A",
            "problem_solution_fit": "N/A",
            "feasibility_level": "N/A",
            "revenue_potential": "N/A",
            "potential_for_growth": "N/A"
        }

# New function for market research analysis
def analyze_market_research(idea: str) -> dict:
    prompt = f"""
    You are a market research expert for startup ideas.

    Analyze the following startup idea and respond ONLY in a clean JSON object without explanation:

    Startup Idea: "{idea}"

    Return JSON with the following keys:
    - market_size: Small/Medium/Large
    - target_audience: Who is most likely to use or benefit from this product?
    - competitors: List the main competitors in the market
    - market_trends: Describe current trends related to the idea
    - market_opportunity: High/Medium/Low
    - barriers_to_entry: Low/Moderate/High
    - customer_acquisition_cost: Low/Moderate/High
    - scalability: Low/Medium/High
    - growth_potential: Estimate the idea's ability to grow over time
    - revenue_potential: Estimate the possible revenue this idea can generate
    """

    print("Sending to LLM for market research...")
    response = model.generate_content(prompt)
    raw_text = response.text.strip()
    '''print("Raw LLM response:", raw_text)'''

    try:
        # Extract JSON from possible markdown formatting
        if raw_text.startswith("```json"):
            raw_text = raw_text.lstrip("```json").rstrip("```").strip()

        result = json.loads(raw_text)
        return result
    except json.JSONDecodeError:
        print("Error parsing response:", raw_text)
        return {
            "market_size": "N/A",
            "competitors": "N/A",
            "trends": "N/A",
            "market_opportunity": "N/A",
            "barriers_to_entry": "N/A",
            "customer_acquisition_cost": "N/A",
            "scalability": "N/A"
        }