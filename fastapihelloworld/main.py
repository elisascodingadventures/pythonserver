from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount a directory named 'static' located in the same directory as this script
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=PlainTextResponse)
async def hello_world():
    return "Hello, World!"

@app.get("/hello-gif", response_class=HTMLResponse)
async def get_hello_gif():
    # Reference the GIF using a URL path, not the file system path
    return """
    <html>
        <head>
            <title>Hello GIF</title>
            <style>
                body { background-color: white; }
                img { display: block; margin: 0 auto; }
            </style>
        </head>
        <body>
            <img src="/static/hello.gif" alt="Hello GIF">
        </body>
    </html>
    """
