from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_item(q: str = None):
    if q:
        return {"message": f"Item searched for: {q}"}
    return {"message": "Welcome to the item search! Please add a query string `q` to search."}
