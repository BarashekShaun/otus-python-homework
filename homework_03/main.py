from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/ping/")
def index():
    return {"message": "pong"}


if __name__ == '__main__':
    uvicorn.run(app)
