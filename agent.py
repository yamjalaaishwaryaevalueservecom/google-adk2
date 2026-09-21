from google.adk.agents.llm_agent import Agent
import pandas as pd

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge. Keep with answers crisp',
)
