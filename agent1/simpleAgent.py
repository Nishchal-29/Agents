import os
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

agent = Agent(
    model = Groq(id = "llama3-70b-8192"),
    description = "You are an assistant who could fetch results from web to show news about given topic by user in a short paragraph for each news",
    tools = [DuckDuckGoTools()],
    markdown = True
)

agent.print_response("What is the latest news about AI ?")