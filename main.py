from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    Product: str
    Price: float


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/cart")
def get_cart(item: Item):
    print(item)
    return {f"payload: {item}"}



