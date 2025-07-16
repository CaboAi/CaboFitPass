#!/bin/bash

# Activate virtual environment
source crewai-env/bin/activate

# Install CrewAI and dependencies
pip install crewai crewai-tools 'crewai-tools[mcp]' python-dotenv

# Install additional useful packages
pip install langchain langchain-openai langchain-anthropic

# Create requirements file
pip freeze > requirements_crewai.txt

echo "CrewAI installation complete!"