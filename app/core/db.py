from motor.motor_asyncio import AsyncIOMotorClient
from app.core.settings import settings

DATABASE_NAME: str = settings.DATABASE_NAME

client = AsyncIOMotorClient(settings.MONGODB_URL)
db = client[settings.DATABASE_NAME]
