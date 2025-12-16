import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]

users = db["users"]
topics = db["topics"]
questions = db["questions"]
test_results = db["test_results"]
