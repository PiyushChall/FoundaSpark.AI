import os
import google.generativeai as genai
import json  # Use safe JSON parsing instead of eval
from dotenv import load_dotenv
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Use env var in production

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

    print("Sending to LLM for idea analysis...")
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
    - barriers_to_entry: Low/Medium/High
    - customer_acquisition_cost: Low/Medium/High
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


def analyze_problem_solution(idea: str) -> dict:
    prompt = f"""
    You are an expert in identifying problem-solution fit.

    Analyze this startup idea and respond ONLY in a clean JSON object:

    Startup Idea: "{idea}"

    Return JSON with:
    - core_problem: Define the core problem by analysing the idea
    - proposed_solution: Define what is being implemented in the solution
    - solution_alignment: Low/Medium/High
    - problem_severity: Low/Medium/High
    - urgency_to_solve: Low/Medium/High
    """

    print("Sending to LLM for problem solution analysis...")
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
            "core_problem": "N/A",
            "proposed_solution": "N/A",
            "solution_alignment": "N/A",
            "problem_severity": "N/A",
            "urgency_to_solve": "N/A",
        }

def analyze_uvp(idea: str) -> dict:
    prompt = f"""
    You are a Unique Value Proposition (UVP) specialist.

    Analyze the following startup idea and respond ONLY in a clean JSON object:

    Startup Idea: "{idea}"

    Return JSON with:
    - uvp_summary: Define a one-sentence unique value proposition that explains why this idea is different and valuable
    - key_differentiator: List 3-5 key features or aspects that make the product/service stand out
    - uniqueness_score: rate from 1-10
    - customer_benefit: What is the main value or outcome the customer receives?
    - customer_benefit_clarity: Clear/Vague
    - is_uvp_strong: Yes/No
    """

    print("Sending to LLM for UVP analysis...")
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
            "uvp_summary": "N/A",
            "key_differentiator": "N/A",
            "uniqueness_score": "N/A",
            "customer_benefit_clarity": "N/A",
            "is_uvp_strong": "N/A",
        }

def analyze_business_model(idea: str) -> dict:
    prompt = f"""
    You are a business model expert.

    Analyze the startup idea and respond ONLY in a clean JSON object:

    Startup Idea: "{idea}"

    Return JSON with:
    - revenue_streams: Define the best revenue streams for the startup idea
    - cost_structure: Elaborate on the cost structure of the idea
    - monetization_strategy: Define the best monetization strategy for this startup idea
    - scalability_of_model: Low/Medium/High
    - recurring_revenue: Yes/No
    - estimated_break_even_time: What would be the estimate break even time in months based on the startup idea
    """

    print("Sending to LLM for business model analysis...")
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
            "revenue_streams": "N/A",
            "cost_structure": "N/A",
            "monetization_strategy": "N/A",
            "scalability_of_model": "N/A",
            "recurring_revenue": "N/A",
            "estimated_break_even_time": "N/A",
        }

def generate_pitch_deck_summary(idea: str) -> dict:
    prompt = f"""
    You are a professional startup pitch deck creator.

    Based on the following startup idea, generate a detailed JSON summary that would be used to prepare slides for a professional investor pitch deck.

    Startup Idea: "{idea}"

    Return in JSON format with:
    - title: Catchy name for the startup
    - one_liner: A one-line description that summarizes the startup's mission or product
    - problem: Briefly describe the core problem being solved
    - solution: How the startup solves that problem uniquely and effectively
    - market_size: Describe the potential market size (quantified if possible)
    - business_model: Explain how the startup will make money
    - traction: Mention any traction or progress made (or say "Early Stage" if none)
    - team: Describe the founding team and their relevant experience
    - funding_ask: Mention the funding amount required and how it will be used (e.g., team, product, marketing)
    """

    print("Sending to LLM for pitch deck generation...")
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
            "title": "N/A",
            "one_liner": "N/A",
            "problem": "N/A",
            "solution": "N/A",
            "market_size": "N/A",
            "business_model": "N/A",
            "traction": "N/A",
            "team": "N/A",
            "funding_ask": "N/A",
        }