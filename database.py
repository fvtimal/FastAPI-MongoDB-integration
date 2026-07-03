from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017")

db = client.bookstore #creates db

books_collection = db.books  #creates collection





