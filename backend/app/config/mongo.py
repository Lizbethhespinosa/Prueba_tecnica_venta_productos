from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://host.docker.internal:27017"

client = AsyncIOMotorClient(MONGO_URL)

mongo_db = client["pruebamongo"]

purchase_collection = mongo_db["purchases"]