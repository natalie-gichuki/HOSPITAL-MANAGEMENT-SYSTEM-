import os
from dotenv import load_dotenv

load_dotenv() # This function will load environment variables from the .env files

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./hospital.db")
# The default database URL is set to a SQLite database named hospital.db in the current directory.