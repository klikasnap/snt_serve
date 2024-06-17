from functools import partial
from typing import Any, Callable, Dict, List, Union

from fastapi import Request
from fastapi.responses import UJSONResponse
from starlette.templating import Jinja2Templates

from . import globals
from .exceptions import CDiTypeError, CDKeyError, CDTypeError

# Constants
STAT_PRIO = ["phrase", "description", "spec", "spec_link"]
DEF_DEET = {
    1: "Information",
    2: "Success",
    3: "Redirect",
    4: "Client Error",
    5: "Server Error",
    7: "Developer Error",
}
DEF_MSG = {
    4: "The client has erred.",
    5: "The server has erred.",
    7: "Thy underpaid yet overworked developer hath erred.",
}
DEF_ERR = {
    1: False,
    2: False,
    3: False,
    4: True,
    5: True,
    7: True,
}


def fetch_flash(request: Request):
    return request.session.pop("_messages") if "_messages" in request.session else []


TEMPLATES = Jinja2Templates(directory="api/templates")
TEMPLATES.env.globals["fetch_flash"] = fetch_flash


class CuRs:
    @staticmethod
    def rjson(  # noqa: C901
        status_code: int,
        detail: Optional[str] = None,
        message: Optional[str] = None,
        error: bool = None,
    ):
        c0 = int(str(status_code)[0])

        if error is None:
            error = DEF_ERR.get(c0, False)

        if rci := CONSTANTS_YML.dir(f"http/code/{status_code}", None):
            rci = rci.copy()
            ci = {}
            for i in STAT_PRIO:
                if (rcip := rci.pop(i, "U2VDckV0")) and (rcip != "U2VDckV0"):
                    ci[i] = rcip

            gi = {}
            rgi = CONSTANTS_YML.dir(f"http/group/{c0}").copy()
            for i in STAT_PRIO:
                if (rgip := rgi.pop(i, "U2VDckV0")) and (rgip != "U2VDckV0"):
                    gi[i] = rgip
            if (rgis := rgi.pop("subgroup", "U2VDckV0")) and (rgis != "U2VDckV0"):
                rgis = rgis.copy()
                if (rgisc := rgis.pop(str(status_code)[1], "U2VDckV0")) and (
                    rgisc != "U2VDckV0"
                ):
                    gi["subgroup"] = rgisc

            status = {"code": status_code, **ci, **rci, "group": {**gi, **rgi}}
        else:
            status = {"code": status_code}

        if c0 == 1:
            status_code = 200
        elif c0 == 7:
            status_code = 500

        content = {}

        if detail:= (detail or DEF_DEET.get(c0, None)):
            content["detail"] = detail

        if message:= (message or DEF_MSG.get(c0, None)):
            content["message"] = message

        content["error"] = DEF_ERR.get(c0, False) if error is None else error

        return [status_code, content, status]

    def json(
        status_code: int,
        detail: str = None,
        message: str = None,
        error: bool = None,
        json: Dict[str, Any] = None,
        *args,
        **kwargs,
    ):

        if json is None:
            json = {}

        status_code, content, status = CuRs.rjson(
            status_code, detail, message, error
        ).copy()

        return UJSONResponse(
            status_code=status_code,
            content={
                **content,
                **json,
                "status": status,
            },
            *args,
            **kwargs,
        )

    def tpl(
        request: Request, tpl: str
    ) -> Callable[[str, str], TEMPLATES.TemplateResponse]:
        def inner(
            message: str, category: str = "primary", *args, **kwargs
        ) -> TEMPLATES.TemplateResponse:
            if "_messages" not in request.session:
                request.session["_messages"] = []
            request.session["_messages"].append(
                {"message": message, "category": category}
            )
            return TEMPLATES.TemplateResponse(
                tpl, {"request": request}, *args, **kwargs
            )

        return inner


CONSTANTS_YML = globals.CONSTANTS_YML = CustomDict(globals.CONSTANTS_YML)
