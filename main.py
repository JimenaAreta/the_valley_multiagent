from agents import research_team
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    research_team.print_response(
        "Impacto de la IA en la investigación periodística",
        stream=True,
    )
