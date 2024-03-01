from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/test")
async def test_endpoint():
    return {"message": "This is a test endpoint!"}