import uvicorn
from fastapi import FastAPI
from endpoints import random_values

app = FastAPI(title="HW FastAPI")

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


if __name__ == '__main__':
    uvicorn.run("main:app", port=5050, host='0.0.0.0', reload=True)
    # uvicorn.run("main:app", port=5050, host='0.0.0.0', workers=8)
