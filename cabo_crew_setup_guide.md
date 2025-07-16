# Cabo Tourism Research Crew - Complete Setup Guide

## 1. Prerequisites & Installation

### Environment Setup
```bash
# Activate your CrewAI virtual environment
source crewai-env/bin/activate

# Install additional required packages
pip install langchain-openai langchain-anthropic langchain-google-genai
pip install pydantic python-dotenv requests beautifulsoup4
pip install pandas numpy matplotlib seaborn  # For data analysis
pip install streamlit  # Optional: for web interface
```

### Required API Keys
Create a `.env` file in your project directory:

```env
# Core LLM APIs
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
GOOGLE_API_KEY=your_google_api_key_here

# Search & Web Tools
SERPER_API_KEY=your_serper_api_key_here
BROWSERLESS_API_KEY=your_browserless_api_key_here

# Tourism-Specific APIs
GOOGLE_PLACES_API_KEY=your_google_places_api_key_here
TRIPADVISOR_API_KEY=your_tripadvisor_api_key_here

# Competitive Intelligence (Optional)
SEMRUSH_API_KEY=your_semrush_api_key_here
SIMILARWEB_API_KEY=your_similarweb_api_key_here

# Social Media APIs (Optional)
TWITTER_BEARER_TOKEN=your_twitter_bearer_token_here
FACEBOOK_ACCESS_TOKEN=your_facebook_access_token_here

# Database (Optional for persistence)
DATABASE_URL=postgresql://user:password@localhost/cabo_research
```

## 2. LLM Recommendations by Agent/Role

### Market Research Specialist
**Recommended: Claude 3.5 Sonnet**
- Best for analytical thinking and data synthesis
- Excellent at processing large amounts of information
- Strong reasoning capabilities for market analysis

```python
from langchain_anthropic import ChatAnthropic

market_researcher_llm = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    temperature=0.1,  # Low temperature for factual analysis
    max_tokens=4000
)
```

### Customer Insights Analyst
**Recommended: GPT-4 Turbo**
- Superior for sentiment analysis and emotional understanding
- Excellent multilingual capabilities (English/Spanish)
- Good at reading between the lines in customer feedback

```python
from langchain_openai import ChatOpenAI

sentiment_analyst_llm = ChatOpenAI(
    model="gpt-4-turbo-preview",
    temperature=0.2,  # Slightly higher for nuanced interpretation
    max_tokens=4000
)
```

### Product Strategist
**Recommended: Claude 3.5 Sonnet**
- Excellent strategic thinking and planning
- Good at technical product specifications
- Strong logical reasoning for feasibility analysis

```python
product_strategist_llm = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    temperature=0.3,  # Moderate creativity for product ideas
    max_tokens=4000
)
```

### Business Analyst
**Recommended: GPT-4 Turbo**
- Strong at financial modeling and ROI calculations
- Good understanding of business operations
- Reliable for structured analysis

```python
business_analyst_llm = ChatOpenAI(
    model="gpt-4-turbo-preview",
    temperature=0.1,  # Low temperature for precise analysis
    max_tokens=4000
)
```

### Implementation Strategist
**Recommended: Claude 3.5 Sonnet**
- Excellent at creating detailed plans and roadmaps
- Good at considering multiple variables and constraints
- Strong at risk assessment and mitigation

```python
implementation_llm = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    temperature=0.2,  # Low-moderate for structured planning
    max_tokens=4000
)
```

## 3. Cost-Optimized Alternative Setup

### Budget-Friendly Option
For lower costs while maintaining quality:

```python
# Use GPT-4 Mini for most agents
budget_llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    max_tokens=2000
)

# Use Claude 3.5 Sonnet only for the most critical agent
premium_llm = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    temperature=0.1,
    max_tokens=4000
)

# Assign premium LLM to Market Researcher (most important)
# Use budget LLM for other agents
```

## 4. Enhanced Crew Configuration

Create `cabo_crew_production.py`:

```python
#!/usr/bin/env python3
"""
Production-ready Cabo Tourism Research Crew with optimized LLM assignments
"""

import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, WebsiteSearchTool
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

# LLM Configuration
def get_llm_config():
    """Configure LLMs for different agent types"""
    return {
        "research": ChatAnthropic(
            model="claude-3-5-sonnet-20241022",
            temperature=0.1,
            max_tokens=4000
        ),
        "analysis": ChatOpenAI(
            model="gpt-4-turbo-preview", 
            temperature=0.2,
            max_tokens=4000
        ),
        "strategy": ChatAnthropic(
            model="claude-3-5-sonnet-20241022",
            temperature=0.3,
            max_tokens=4000
        ),
        "business": ChatOpenAI(
            model="gpt-4-turbo-preview",
            temperature=0.1,
            max_tokens=4000
        )
    }

# Budget-friendly alternative
def get_budget_llm_config():
    """Budget-friendly LLM configuration"""
    premium_llm = ChatAnthropic(
        model="claude-3-5-sonnet-20241022",
        temperature=0.1,
        max_tokens=4000
    )
    
    budget_llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2,
        max_tokens=2000
    )
    
    return {
        "research": premium_llm,  # Most important agent gets premium
        "analysis": budget_llm,
        "strategy": budget_llm, 
        "business": budget_llm
    }

def create_agents(llms):
    """Create optimized agents with appropriate LLMs"""
    
    tools = [SerperDevTool(), WebsiteSearchTool()]
    
    agents = {
        "researcher": Agent(
            role="Cabo Tourism Market Research Specialist",
            goal="Identify specific market gaps in Cabo San Lucas tourism with data-driven insights",
            backstory="""Expert market researcher with 15+ years in Mexican tourism markets. 
            Deep understanding of Los Cabos dynamics and tourist behavior patterns.""",
            tools=tools,
            llm=llms["research"],
            max_iter=5,
            verbose=True
        ),
        
        "sentiment_analyst": Agent(
            role="Customer Experience & Sentiment Analyst", 
            goal="Extract actionable insights from customer feedback across platforms",
            backstory="""Specialist in multilingual sentiment analysis with expertise 
            in hospitality customer behavior and satisfaction metrics.""",
            tools=tools,
            llm=llms["analysis"],
            max_iter=4,
            verbose=True
        ),
        
        "product_strategist": Agent(
            role="AI Product Strategy Specialist",
            goal="Design innovative AI solutions for Cabo tourism market challenges", 
            backstory="""Product strategist with 10+ successful AI product launches 
            in hospitality. Expert in bilingual AI solutions and Mexican market dynamics.""",
            tools=tools,
            llm=llms["strategy"],
            max_iter=4,
            verbose=True
        ),
        
        "business_analyst": Agent(
            role="Tourism Business Operations Analyst",
            goal="Ensure proposed solutions are operationally feasible and profitable",
            backstory="""Business analyst with hands-on experience working with 
            50+ hotels and tour operators in Los Cabos. Expert in implementation challenges.""",
            tools=tools,
            llm=llms["business"],
            max_iter=3,
            verbose=True
        )
    }
    
    return agents

# Usage examples
if __name__ == "__main__":
    # Choose your configuration
    print("LLM Configuration Options:")
    print("1. Premium (Claude + GPT-4 Turbo): ~$50-100 per full analysis")
    print("2. Budget (Claude + GPT-4 Mini): ~$15-30 per full analysis")
    
    # Use premium configuration
    llms = get_llm_config()
    # Or use budget configuration
    # llms = get_budget_llm_config()
    
    agents = create_agents(llms)
    print("Agents created successfully with optimized LLM assignments")
```

## 5. API Key Acquisition Guide

### Free/Low-Cost APIs
1. **Serper (Google Search)**: Free tier with 2,500 searches/month
   - Sign up: https://serper.dev/
   
2. **Google Places API**: $5 credit monthly, ~1000 requests free
   - Enable: Google Cloud Console → Places API
   
3. **OpenAI**: $5 free credit for new accounts
   - Sign up: https://platform.openai.com/

### Premium APIs (Optional)
1. **Anthropic Claude**: Pay-per-use, no free tier
   - Sign up: https://console.anthropic.com/
   
2. **TripAdvisor API**: Contact for access
   - Limited public API availability
   
3. **SEMrush/SimilarWeb**: Expensive enterprise tools
   - Consider alternatives like Serpstat or Ahrefs

## 6. Cost Estimation

### Premium Configuration (Full Analysis)
- **Market Research Task**: ~$15-25 (Claude Sonnet)
- **Sentiment Analysis**: ~$10-20 (GPT-4 Turbo) 
- **Product Strategy**: ~$10-20 (Claude Sonnet)
- **Business Analysis**: ~$8-15 (GPT-4 Turbo)
- **Implementation Planning**: ~$10-15 (Claude Sonnet)
- **Total per full analysis**: ~$53-95

### Budget Configuration (Full Analysis)
- **Market Research**: ~$15-25 (Claude Sonnet)
- **Other tasks**: ~$3-8 each (GPT-4 Mini)
- **Total per analysis**: ~$27-49

### Cost Optimization Tips
1. **Use caching**: Avoid repeat API calls
2. **Implement rate limiting**: Control token usage
3. **Start with budget config**: Upgrade specific agents as needed
4. **Batch similar queries**: Reduce total API calls

## 7. Quick Start Commands

```bash
# 1. Set up environment
source crewai-env/bin/activate
pip install -r requirements_crewai.txt

# 2. Create .env file with your API keys
cp .env.example .env
# Edit .env with your actual API keys

# 3. Test basic setup
python3 -c "from crewai import Agent; print('CrewAI ready!')"

# 4. Run the enhanced crew
python3 cabo_market_research_crew_improved.py

# 5. Monitor costs
# Check API usage in respective dashboards
```

## 8. Troubleshooting Common Issues

### API Key Issues
- Verify all keys are correctly set in `.env`
- Check API quotas and billing status
- Test individual APIs before running full crew

### Memory/Performance Issues
- Reduce `max_tokens` for budget constraints
- Implement task chunking for large analyses
- Use `max_rpm` parameter to control rate limits

### Quality Issues
- Increase temperature for more creative tasks
- Decrease temperature for factual analysis
- Add more specific instructions in agent backstories

This setup will give you a production-ready research crew optimized for your Cabo tourism market analysis needs.