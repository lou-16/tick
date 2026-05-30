from fastapi import FastAPI

app = FastAPI();

@app.get('/')
def read_root():
    return { "hello" : "world" }

@app.get('/{id}')
def read_id(id): 
    return { "id" : id}