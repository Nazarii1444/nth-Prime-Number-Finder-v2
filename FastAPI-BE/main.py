from get_prime import find_nth_prime_number
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/ping")
async def ping():
    return {"Pong!"}


@app.post("/get_prime/{n}")
async def calc_task(n: int = Query(..., ge=1, le=100000000)):
    if 1 <= n <= 1000:
        return find_nth_prime_number(n)
    else:
        ...


@app.get("/")
async def root():
    return {"Hello World!"}

