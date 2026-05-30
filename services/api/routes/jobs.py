from fastapi import FastAPI;
from fastapi import Request;

route = FastAPI()

@route.post('/')
async def postJobs(request: Request):
    await body = request.body;
        