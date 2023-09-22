from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DataItem(BaseModel):
    innerHTML: str

@app.post("/receive-data/")
async def receive_data(data: DataItem):
    print("Received Data:")
    print(data.innerHTML)
    return {"message": "Data received successfully"}
