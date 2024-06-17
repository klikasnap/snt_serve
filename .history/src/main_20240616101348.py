import time
import traceback

from fastapi import FastAPI, Request, Response
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse, UJSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.templating import _TemplateResponse

from .api.globals import ENVIRON
from .api.routers import users
from .api.utils import TEMPLATES, CuRs

description = """
api.hyaku.download
"""

middleware = [Middleware(SessionMiddleware, secret_key=ENVIRON["JWT_SECRET"])]
app = FastAPI(
    title="api.hyaku.download",
    description=description,
    version="0.0.1",
    terms_of_service="http://hyaku.download/tos",
    contact={
        "name": "whi_ne",
        "url": "https://whinyaan.xyz",
        "email": "whinyaan@protonmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://choosealicense.com/licenses/mit/",
    },
    docs_url=None,
    redoc_url=None,
    middleware=middleware,
)

app.include_router(users.router, prefix="/users", tags=["users"])


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    try:
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response
    except Exception:  # noqa: BLE001
        return CuRs.json(
            status_code=500,
            message="Error occured",
            json={"traceback": traceback.format_exc()},
        )


app.mount("/static/", StaticFiles(directory="api/static"), name="static")
app.mount(
    "/templates/", StaticFiles(directory="api/templates", html=True), name="templates"
)


@app.get("", include_in_schema=False, status_code=200)
def docs(response: Response) -> HTMLResponse:
    response.status_code = 200
    return get_swagger_ui_html(
        openapi_url=app.openapi_url, # type: ignore[arg-type]
        title=app.title + " - Docs",
        swagger_css_url="/static/stylesheets/docs.css",
    )


@app.post("/code/{code}")
def code(code: int) -> UJSONResponse:
    return CuRs.json(status_code=code)


@app.get("/code/{code}")
def code(request: Request, code: int) -> _TemplateResponse:
    status_code, content, status = CuRs.rjson(status_code=code).copy()
    return TEMPLATES.TemplateResponse(
        "code.j2.html",
        {
            "request": request,
            "content": content,
            "status": {"code": status_code, **status.copy()},
        },
        status_code=status_code,
    )


# @app.api_route(
#     "/{path_name:path}", include_in_schema=False, status_code=403,
#     methods=[
#         "HEAD", "GET", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"
# ])
# async def catch_all(request: Request, path_name: str):
#     return {
#         "message": "Error occured",
#         "error": "Request Forbidden",
#         "request_method": request.method,
#         "path_name": path_name
#     }
