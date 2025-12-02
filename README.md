# FoundaSpark.AI – Startup Idea Validator & Pitch-Deck Generator

## Project Overview  
FoundaSpark.AI is a web-app built to help entrepreneurs, innovators, and early-stage startup founders quickly validate their business ideas and generate polished pitch decks. Users submit a brief description of their idea — the system runs a multi-agent AI pipeline that analyses market potential, competition, problem–solution fit, unique value proposition (UVP), and business-model viability. In less than a few minutes, FoundaSpark.AI returns a comprehensive validation report along with a ready-to-use pitch deck. This significantly reduces the entry barrier for new founders by offering professional-level evaluation without the need for consulting.

## Technologies & Architecture  
- **Backend**: Python (Flask / FastAPI)  
- **Frontend**: HTML / CSS / JavaScript templates  
- **Deployment**: Hosted on cloud (as per repository settings)  
- **AI Core**: Multi-agent AI architecture — six specialized agents performing distinct analysis tasks: IdeaAnalyzer, MarketResearcher, ProblemSolutionAnalyzer, UniqueValuePropositionAnalyzer, BusinessModelAnalyzer, and PitchDeckGenerator.  
- **Output Generation**: Dynamically generated pitch decks (PDF or presentation format) along with detailed analytical reports.

## My Role & Contributions  
I developed the full-stack solution end-to-end — designing the AI-agent architecture, building backend API routes to handle input, orchestrate agent workflow, and assemble the results. I implemented the UI to accept user inputs and display the analysis. I integrated the deck-generation logic and managed deployment on a live server. I also wrote documentation (README, usage instructions) to make the tool usable by first-time startup founders.

## Challenges & Solutions  
- **Challenge**: Combining multiple AI-agents to produce coherent, non-redundant analysis — especially avoiding overlap between market research, problem/solution fit, and UVP evaluation.  
- **Solution**: Designed a structured pipeline where each agent receives clearly defined input and purpose; enforced modular, isolated reasoning; aggregated results carefully to avoid duplication, and added manual consistency checks before output.  
- **Challenge**: Generating a professional-looking pitch deck dynamically.  
- **Solution**: Built template-driven deck generator with clean design and generated final output in standard formats, making it ready to present to investors.

## Usage / Demo  
You can try the live version here:  
[Live App → https://rising-melania-piyushchall-3f97946b.koyeb.app/](https://rising-melania-piyushchall-3f97946b.koyeb.app/)  

Clone the repo and follow instructions in `requirements.txt` to set up locally.

---

*Built by Piyush Chall — MIT Licensed*  
