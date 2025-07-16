# CaboAiCrew - AI-Powered Tourism Market Research Platform

An advanced market research platform using CrewAI multi-agent framework to analyze tourism opportunities in Cabo San Lucas, Mexico.

## 🎯 Overview

CaboFitPass leverages AI agents to conduct comprehensive market research for tourism businesses in Los Cabos. Our platform identifies market gaps, analyzes customer sentiment, and provides actionable insights for developing AI-powered solutions in the hospitality sector.

## 🚀 Features

- **Multi-Agent Research System**: 5 specialized AI agents working collaboratively
- **Bilingual Support**: English and Spanish market analysis
- **Real-Time Data Analysis**: Integration with tourism APIs and web data
- **Structured Insights**: Actionable reports with ROI projections
- **MCP Integration**: Model Context Protocol support for enhanced capabilities

## 🤖 AI Agents

1. **Market Research Specialist**: Identifies gaps in Cabo tourism market
2. **Customer Insights Analyst**: Extracts sentiment from reviews and feedback
3. **Product Strategist**: Designs AI-powered solutions for identified gaps
4. **Business Analyst**: Ensures operational feasibility and ROI
5. **Implementation Strategist**: Creates detailed go-to-market plans

## 📋 Prerequisites

- Python 3.12+
- OpenAI API key
- Anthropic API key (optional, for premium features)
- Serper API key (for web search)

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/CaboAi/CaboFitPass.git
cd CaboFitPass
```

2. **Create virtual environment**
```bash
python3 -m venv crewai-env
source crewai-env/bin/activate  # On Windows: crewai-env\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements_cabo_crew.txt
```

4. **Set up environment variables**
```bash
cp .env.template .env
# Edit .env with your API keys
```

## 💡 Usage

### Basic Example
```python
# Run the basic CrewAI example
python3 crewai_example.py
```

### Cabo Tourism Market Research
```python
# Run the enhanced Cabo tourism research crew
python3 cabo_market_research_crew_improved.py
```

### MCP Integration Example
```python
# Explore MCP server integration
python3 crewai_mcp_example.py
```

## 📊 Example Output

The crew generates comprehensive reports including:
- Market gap analysis with data-driven insights
- Customer sentiment analysis from multiple platforms
- Product specifications with ROI projections
- Implementation roadmaps with partnership strategies
- Competitive intelligence reports

## 💰 Cost Estimates

- **Premium Configuration** (Claude 3.5 + GPT-4): ~$50-100 per analysis
- **Budget Configuration** (Mixed models): ~$15-30 per analysis

## 🔧 Configuration Options

### LLM Selection
- **Claude 3.5 Sonnet**: Best for strategic analysis
- **GPT-4 Turbo**: Superior for sentiment analysis
- **GPT-4 Mini**: Budget-friendly option

### Crew Configuration
```python
crew = Crew(
    agents=[...],
    tasks=[...],
    memory=True,      # Enable context retention
    cache=True,       # Enable result caching
    max_rpm=10,       # Rate limiting
    verbose=True      # Detailed logging
)
```

## 📁 Project Structure

```
CaboFitPass/
├── crewai_example.py              # Basic CrewAI example
├── crewai_mcp_example.py          # MCP integration examples
├── cabo_market_research_crew_improved.py  # Enhanced research crew
├── cabo_mcp_integration_suggestions.py    # MCP server examples
├── cabo_crew_analysis_and_suggestions.md  # Detailed analysis
├── cabo_crew_setup_guide.md       # Setup instructions
├── requirements_cabo_crew.txt     # Python dependencies
├── .env.template                  # Environment template
└── README.md                      # This file
```

## 🔑 API Keys Required

### Essential
- **OpenAI**: GPT-4 models for analysis
- **Serper**: Google search capabilities

### Optional but Recommended
- **Anthropic**: Claude models for premium analysis
- **Google Places**: Tourism business data
- **TripAdvisor**: Review data access

## 🚧 Roadmap

- [ ] Web interface using Streamlit
- [ ] PostgreSQL integration for data persistence
- [ ] Advanced visualization dashboards
- [ ] Automated report scheduling
- [ ] WhatsApp/Telegram bot integration
- [ ] Real-time market monitoring

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

**CaboAi** - AI Solutions for Los Cabos Tourism  
Email: caboconnectai@gmail.com  
Location: Cabo San Lucas, Mexico

## 📄 License

This project is proprietary software owned by CaboAi.

---

Built with ❤️ for the Los Cabos tourism industry using [CrewAI](https://www.crewai.com/) and Claude Code.
