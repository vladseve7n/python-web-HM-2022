import uvicorn
from fastapi import FastAPI, Request
from endpoints import random_values
import time

app = FastAPI(
    title="HW FastAPI",
    description="App for doing corse's HW",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(random_values.router, prefix="/random", tags=["Random values generator"])


@app.get("/")
async def root():
    return {"message": "Hello this is project for course's home works!"}


@app.on_event("startup")
async def startup():
    print('App has started!')


@app.on_event("shutdown")
async def shutdown():
    print('App has finished!')


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):  # noqa: D103
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


if __name__ == '__main__':
    uvicorn.run("main:app", port=5050, host='0.0.0.0', reload=True)
    # uvicorn.run("main:app", port=5050, host='0.0.0.0', workers=8)
