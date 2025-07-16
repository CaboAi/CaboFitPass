#!/usr/bin/env python3
"""
CrewAI Example - Research Team
This example demonstrates how to create a crew of AI agents that work together.
"""

import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, WebsiteSearchTool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize tools
search_tool = SerperDevTool()
web_search_tool = WebsiteSearchTool()

# Create agents
researcher = Agent(
    role='Senior Research Analyst',
    goal='Research and analyze information about {topic}',
    backstory="""You are an expert research analyst with years of experience in
    gathering and analyzing information from various sources. You excel at finding
    relevant data and presenting it in a clear, actionable format.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, web_search_tool]
)

writer = Agent(
    role='Content Writer',
    goal='Create compelling content based on research findings',
    backstory="""You are a skilled content writer who specializes in transforming
    complex research into engaging, easy-to-understand content. You have a talent
    for structuring information logically and writing in a clear, persuasive style.""",
    verbose=True,
    allow_delegation=False
)

editor = Agent(
    role='Senior Editor',
    goal='Review and refine content for quality and accuracy',
    backstory="""You are a meticulous editor with a keen eye for detail. You ensure
    all content is accurate, well-structured, and polished before publication.""",
    verbose=True,
    allow_delegation=False
)

# Create tasks
research_task = Task(
    description="""Research {topic} thoroughly. Gather information about:
    1. Current trends and developments
    2. Key statistics and data points
    3. Expert opinions and insights
    4. Relevant case studies or examples
    
    Compile your findings into a comprehensive research report.""",
    expected_output="A detailed research report with citations and key findings",
    agent=researcher
)

writing_task = Task(
    description="""Based on the research report, create an engaging article about {topic}.
    The article should:
    1. Have a compelling introduction
    2. Present key findings in an organized manner
    3. Include relevant examples and data
    4. End with actionable insights or conclusions
    
    Target length: 800-1000 words""",
    expected_output="A well-written article ready for publication",
    agent=writer,
    context=[research_task]
)

editing_task = Task(
    description="""Review and edit the article for:
    1. Grammar and spelling errors
    2. Clarity and readability
    3. Logical flow and structure
    4. Accuracy of information
    5. Consistency in tone and style
    
    Make necessary improvements and provide the final version.""",
    expected_output="A polished, publication-ready article",
    agent=editor,
    context=[writing_task]
)

# Create the crew
research_crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, writing_task, editing_task],
    process=Process.sequential,  # Tasks will be executed sequentially
    verbose=True
)

# Example usage
if __name__ == "__main__":
    # Run the crew with a specific topic
    result = research_crew.kickoff(inputs={'topic': 'AI automation for small businesses'})
    
    print("\n" + "="*80)
    print("FINAL RESULT:")
    print("="*80)
    print(result)