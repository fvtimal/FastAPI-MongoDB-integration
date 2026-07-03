from database import books_collection
from models import Book
from fastapi import FastAPI

app = FastAPI()


@app.post("/books")
async def create_books(book: Book):
    await books_collection.insert_one(book.model_dump())

    return {
        "message": "Book added successfully"
    }

@app.get("/books")
async def get_books():
    books = []
    #books = await books_collection.find().to_list(length=100)
    #^^^ to limit num of books/documents to 100

    async for book in books_collection.find():
        book.pop("_id")
        books.append(book)

    return books

@app.put("/books/{title}")
async def update_book(title: str, price: float):
    result = await books_collection.update_one(
        {"title": title},
        {"$set": {"price": price}}
    )

    if result.matched_count == 0:
        return {"message": "Book not found"}

    return {
        "message": "Book updated successfully"
    }

@app.delete("/books/{title}")
async def delete_book(title: str):
    result = await books_collection.delete_one(
        {
            "title": title
        }
    )

    if result.deleted_count == 0:
        return {"message": "Book not found"}

    return {"message": "Book deleted successfully"}
