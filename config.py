import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)        # Loads variables from the .env file.

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")            # Reads the value of OPENAI_API_KEY from environment variables and stores it in a Python variable.
MODEL = "gpt-4o-mini"

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env")