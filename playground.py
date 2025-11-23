from agents import research_team
from agno.os import AgentOS
from dotenv import load_dotenv

load_dotenv()

agent_os = AgentOS(teams=[research_team])
# Get the FastAPI app for the AgentOS
app = agent_os.get_app()

# ************* Run AgentOS *************
if __name__ == "__main__":
    agent_os.serve(app="playground:app", reload=True)