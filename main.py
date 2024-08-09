"""Dummy app."""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <h2>This is a repo with a bad Dockerfile.</h2>
    <iframe width="860" height="515" src="https://www.youtube.com/embed/VZrDxD0Za9I?si=SqlyK4N3x_3TDQzE"
        title="YouTube video player" frameborder="0"
        allow="accelerometer; autoplay; clipboard-write;
        encrypted-media; gyroscope; picture-in-picture;
        web-share" referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen>
    </iframe>
    """


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5002)
