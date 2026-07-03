from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017")

db = client.bookstore #creates reference to db

books_collection = db.books  #creates reference to collection





