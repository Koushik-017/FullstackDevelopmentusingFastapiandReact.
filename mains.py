from typing import Union
from names import names

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware



app = FastAPI()
origins = [

    "http://localhost:3000",

    "localhost:3000"

]

app.add_middleware(

    CORSMiddleware,

    allow_origins=origins,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)

@app.get("/name")
def read_root():
    return {"message": "Welcome to your todo list."}

todos = [
    {
        "id": "1",
        "item": "Read a book."
    },
    {
        "id": "2",
        "item": "Cycle around town."
    }
]
@app.get("/todos")
def read_todos():
    return{"data": todos}

# postAPI
name = []
@app.post("/Upload")
def upload_name(name1: str):
    
    name.append(name1)
    
    return name

# DeleteAPI
@app.delete("todo/{id}")
async def delete_todo(id:int)->dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"Todo with id {id} has been removed."
            }

    return {
        "data": f"Todo with id {id} not found."
    }