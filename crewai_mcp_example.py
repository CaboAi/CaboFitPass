#!/usr/bin/env python3
"""
CrewAI with MCP Integration Example
This example shows how to use MCP servers as tools in CrewAI
"""

import os
from crewai import Agent, Crew, Process, Task
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters, ServerConfig
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Example 1: Using a local MCP server via stdio
def example_stdio_mcp():
    """Example using a local MCP server that communicates via stdio"""
    
    # Configure the MCP server parameters
    server_params = StdioServerParameters(
        command="python3",
        args=["path/to/your/mcp_server.py"],
        env={"PYTHONPATH": os.getcwd()}
    )
    
    # Create MCP adapter and connect to server
    with MCPServerAdapter(server_params) as mcp_tools:
        # Create an agent with MCP tools
        analyst = Agent(
            role='Data Analyst',
            goal='Analyze data using MCP server tools',
            backstory='You are an expert data analyst who uses specialized tools.',
            tools=mcp_tools,  # All tools from the MCP server
            verbose=True
        )
        
        # Create a task
        analysis_task = Task(
            description="Use the available MCP tools to analyze the dataset",
            expected_output="A comprehensive data analysis report",
            agent=analyst
        )
        
        # Create and run the crew
        crew = Crew(
            agents=[analyst],
            tasks=[analysis_task],
            verbose=True
        )
        
        result = crew.kickoff()
        print(result)

# Example 2: Using specific tools from MCP server
def example_filtered_mcp_tools():
    """Example showing how to use only specific tools from an MCP server"""
    
    server_params = StdioServerParameters(
        command="node",
        args=["path/to/mcp-server.js"]
    )
    
    # Filter to use only specific tools
    with MCPServerAdapter(server_params, tool_names=["search", "analyze"]) as mcp_tools:
        researcher = Agent(
            role='Research Specialist',
            goal='Conduct targeted research using specific MCP tools',
            backstory='You specialize in using advanced search and analysis tools.',
            tools=mcp_tools,
            verbose=True
        )
        
        task = Task(
            description="Research the latest trends in AI using the search and analyze tools",
            expected_output="A trend analysis report",
            agent=researcher
        )
        
        crew = Crew(agents=[researcher], tasks=[task])
        result = crew.kickoff()
        print(result)

# Example 3: Using multiple MCP servers
def example_multiple_mcp_servers():
    """Example showing how to combine tools from multiple MCP servers"""
    
    # First MCP server for data tools
    data_server = StdioServerParameters(
        command="python3",
        args=["servers/data_tools_server.py"]
    )
    
    # Second MCP server for web tools
    web_server = StdioServerParameters(
        command="node",
        args=["servers/web_tools_server.js"]
    )
    
    # Create adapters for both servers
    with MCPServerAdapter(data_server) as data_tools, \
         MCPServerAdapter(web_server) as web_tools:
        
        # Combine tools from both servers
        all_tools = list(data_tools) + list(web_tools)
        
        # Create agent with combined tools
        analyst = Agent(
            role='Full-Stack Analyst',
            goal='Analyze data from multiple sources',
            backstory='You can access both data analysis and web scraping tools.',
            tools=all_tools,
            verbose=True
        )
        
        task = Task(
            description="Gather web data and analyze it comprehensively",
            expected_output="An integrated analysis report",
            agent=analyst
        )
        
        crew = Crew(agents=[analyst], tasks=[task])
        result = crew.kickoff()
        print(result)

# Example 4: Using third-party crewai-mcp-toolbox
def example_mcp_toolbox():
    """Example using the crewai-mcp-toolbox package for enhanced integration"""
    
    # Note: This requires: pip install crewai-mcp-toolbox
    try:
        from crewai_mcp_toolbox import MCPToolSet
        
        # Create MCP tool set with automatic type generation
        async def run_with_toolbox():
            async with MCPToolSet(
                server_command="python3",
                server_args=["path/to/mcp_server.py"]
            ) as toolset:
                
                # Get type-safe tools
                tools = await toolset.get_tools()
                
                agent = Agent(
                    role='Advanced Analyst',
                    goal='Use type-safe MCP tools for analysis',
                    backstory='You work with validated, type-safe tools.',
                    tools=tools,
                    verbose=True
                )
                
                task = Task(
                    description="Perform analysis with type-safe tools",
                    expected_output="A validated analysis report",
                    agent=agent
                )
                
                crew = Crew(agents=[agent], tasks=[task])
                result = crew.kickoff()
                print(result)
        
        # Run the async function
        import asyncio
        asyncio.run(run_with_toolbox())
        
    except ImportError:
        print("crewai-mcp-toolbox not installed. Install with: pip install crewai-mcp-toolbox")

# Example 5: Creating a custom MCP server for CrewAI
def create_simple_mcp_server():
    """Example code for a simple MCP server that can be used with CrewAI"""
    
    example_server_code = '''
#!/usr/bin/env python3
"""
Simple MCP Server Example
This server provides tools that can be used by CrewAI agents
"""

import asyncio
import json
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create the server instance
app = Server("example-mcp-server")

# Define tools
@app.tool()
async def calculate(operation: str, a: float, b: float) -> float:
    """Perform basic mathematical operations"""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else float('inf')
    else:
        raise ValueError(f"Unknown operation: {operation}")

@app.tool()
async def get_data(key: str) -> dict:
    """Retrieve data by key"""
    # Example data store
    data_store = {
        "sales": {"q1": 100, "q2": 150, "q3": 200, "q4": 250},
        "customers": {"total": 1000, "active": 750, "new": 100}
    }
    return data_store.get(key, {"error": "Key not found"})

# Run the server
async def main():
    async with stdio_server() as streams:
        await app.run(
            streams.read_stream,
            streams.write_stream,
            app.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
'''
    
    # Save the example server code
    with open("example_mcp_server.py", "w") as f:
        f.write(example_server_code)
    
    print("Created example_mcp_server.py")

if __name__ == "__main__":
    print("CrewAI MCP Integration Examples")
    print("=" * 50)
    print("1. Basic stdio MCP integration")
    print("2. Filtered MCP tools")
    print("3. Multiple MCP servers")
    print("4. Using crewai-mcp-toolbox")
    print("5. Create example MCP server")
    print("\nUncomment the example you want to run in the code.")
    
    # Uncomment the example you want to run:
    # example_stdio_mcp()
    # example_filtered_mcp_tools()
    # example_multiple_mcp_servers()
    # example_mcp_toolbox()
    # create_simple_mcp_server()