from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/cuenta")
async def root():
    a=0
    for i in range(100):
        a+=i
    print(a)
    return {"message": "Se realizó el cálculo"}    

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
