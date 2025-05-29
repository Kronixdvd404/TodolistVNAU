import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tasks.router import router as tasks_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

app.include_router(tasks_router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)
