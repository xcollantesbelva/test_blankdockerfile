"""Dummy app."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_cat_fact():
    return {"response": "This is a repo with a bad Dockerfile."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5002)
