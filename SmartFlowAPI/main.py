from fastapi import FastAPI #get the tools
from pydantic import BaseModel
app = FastAPI() #creates backend app
#@app.get("/health") #creates health endpoint and checks if the endpoint exists in backend system if it is then root() gets executed  
#@app.get("/add/{operator}/{operator2}")
def processing_stuff(message):
    msg = str(message.message)
    up = msg.upper()    
    words = msg.split(" ")
    wcount = len(words)
    return msg,up,wcount #tuple
class Item(BaseModel):
   name: str
   price: float
   description: str | None = None

class Message(BaseModel):
    message: str

@app.post("/process-text")
async def message_process(message:Message):
    ps = processing_stuff(message)
    processed_msg = {
        "original":ps[0],
        "uppercase":ps[1],
        "word_count":ps[2]

    }
    return processed_msg

@app.post("/items/")
async def items_add(item: Item):
    return item


async def add(operator:int,operator2:int):
    total = operator + operator2
    return total
async def root():
    return {'message':'Backend Alive!'} #the format of request to be sent back