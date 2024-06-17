import time
import traceback
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from copy import deepcopy
from typing import Any, Never

from fastapi import Depends, FastAPI, Request, Response
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse, UJSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.templating import _TemplateResponse

from src.api.db import User, create_db_and_tables
from src.api.globals import ENVIRON
from src.api.models.user import UserCreate, UserRead, UserUpdate
from src.api.routers.users import auth_backend, current_active_user, fastapi_users
from src.api.utils import TEMPLATES, CuRs

description = """
api.hyaku.download
"""

middleware = [Middleware(SessionMiddleware, secret_key=ENVIRON["JWT_SECRET"])]

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[Never]:
    await create_db_and_tables()
    yield # type: ignore

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
    lifespan=lifespan,
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)) -> dict[str, str]:
    return {"message": f"Hello {user.email}!"}


app.mount("/static/", StaticFiles(directory="src/api/static"), name="static")
app.mount(
    "/templates/", StaticFiles(directory="src/api/templates", html=True), name="templates",
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
def code_post(code: int) -> UJSONResponse:
    return CuRs.json(status_code=code)

def code_get_output()

@app.get("/code/{code}")
def code_get(request: Request, code: int) -> _TemplateResponse:
    status_code, content, status = deepcopy(CuRs.rjson(status_code=code))
    return TEMPLATES.TemplateResponse(
        "code.j2.html",
        {
            "request": request,
            "content": content,
            "status": {"code": status_code, **deepcopy(status)},
        },
        status_code=status_code,
    )

@app.api_route(
    "/{path_name:path}", include_in_schema=False, status_code=403,
    methods=["GET"])
async def catch_all_get(request: Request, path_name: str) -> dict[str, str]:
    code_get(request, 403)

@app.api_route(
    "/{path_name:path}", include_in_schema=False, status_code=403,
    methods=[
        "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"
])
async def catch_all(request: Request, path_name: str) -> dict[str, str]:
    return {
        "message": "Error occured",
        "error": "Request Forbidden",
        "request_method": request.method,
        "path_name": path_name
    }
