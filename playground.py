from agents import research_team
from agno.playground import Playground, serve_playground_app
from dotenv import load_dotenv

load_dotenv()

app = Playground(agents=[research_team]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)