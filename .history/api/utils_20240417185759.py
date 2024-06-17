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


class CustomDict(dict):
    def _insert(
        self,
        path: str,
        value: Any,
        cdict: Union[Dict[Any, Any], List[Any]],
        idx: int = 0,
        og_path: str = None,
    ) -> Union[Dict[Any, Any], List[Any]]:

        if og_path is None:
            og_path = path

        tep = partial(CDiTypeError, og_path)
        path_ls = path.split("/")
        key = path_ls[0]
        tc = type(cdict)

        try:
            cdict[key]
        except KeyError:
            cdict[key] = {}
        tck = type(cdict[key])

        if len(path_ls) > 1:
            if (tc is list) or (tc.__mro__[-2] is not dict):
                raise tep(idx, tck)
            else:
                if ((tck is list) and (len(path_ls) == 2)) or (tc.__mro__[-2] is dict):
                    op = self._insert(
                        path.replace(f"{key}/", ""), value, cdict[key], idx + 1, og_path
                    )
                    if tc.__mro__[-2] is dict:
                        cdict[key] = op
                    else:
                        cdict[key].append(op)
                    return cdict
                raise tep(idx + 1, tck)
        else:
            if tck is list:
                cdict[key].append(value)
            else:
                cdict[key] = value
            return cdict

    def insert(self, path: str, value: Any) -> Dict[Any, Any]:
        self._insert(path, value, self)

    def _dir(
        self,
        path: str,
        cdict: Union[Dict[Any, Any], List[Any]],
        de: Any,
        idx: int = 0,
        og_path: str = None,
    ) -> Any:

        if og_path is None:
            og_path = path

        path_ls = path.split("/")
        key = path_ls[0]
        tc = type(cdict)

        if len(path_ls) > 1:
            if tc.__mro__[-2] is dict:
                return self._dir(
                    path.replace(f"{key}/", ""), cdict[key], de, idx + 1, og_path
                )
            raise CDTypeError(
                f'`{"/".join(og_path.split("/")[:idx])}` is a {tc.__name__}'
                + ", expected dictionary."
            )
        else:
            try:
                return cdict[key]
            except (KeyError, TypeError):
                if de == "U2VDckV0":
                    raise CDKeyError(
                        f'`{"/".join(og_path.split("/")[:idx + 1])}` cannot be found.'
                    )
                return de

    def dir(self, path: str, de: Any = "U2VDckV0") -> Any:
        return self._dir(path, self, de)


def fetch_flash(request: Request):
    return request.session.pop("_messages") if "_messages" in request.session else []


TEMPLATES = Jinja2Templates(directory="api/templates")
TEMPLATES.env.globals["fetch_flash"] = fetch_flash


class CuRs:
    def rjson(
        status_code: int,
        detail: str = None,
        message: str = None,
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
