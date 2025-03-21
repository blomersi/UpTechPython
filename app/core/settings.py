from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class Settings:
  MONGODB_URL = os.getenv("MONGODB_URL")
  DATABASE_NAME = os.getenv("DATABASE_NAME")

settings = Settings()