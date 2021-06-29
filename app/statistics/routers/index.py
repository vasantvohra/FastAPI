from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(tags=['Index'])


@router.get('/', response_class=HTMLResponse)
def index():
    return """
    <html>
        <head>
            <title>Fast APIs</title>
        </head>
        <body>
            <h1>Go to <a href='/docs'>API docs</a></h1>
        </body>
    </html>
    """
