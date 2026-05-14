import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.getenv("MONGO_URL")

client = AsyncIOMotorClient(MONGO_URL)

mongo_db = client["pruebamongo"]

purchase_collection = mongo_db["purchases"]