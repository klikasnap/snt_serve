from collections.abc import Callable
from copy import deepcopy
from os.path import dirname, realpath
from typing import Any, Optional




def dnrp(file: str, n: Optional[int] = None) -> str:
    """
    Get the directory component of a pathname by n times recursively then return it.

    Args:
    - file (`str`): File to get the directory of.
    - n (`Optional[int]`, optional): Number of times to get up the directory???? Defaults to 1.

    Returns:
    `str`: The directory component got recursively by n times from the given pathname
    """
    op = realpath(file)
    for _ in range(ivnd(n, 1)):
        op = dirname(op)
    return op


def ivnd(var: Any, de: Any) -> Any:
    """
    "If Var None, Default".

    If `var` is `None`, return `de` else `var`.

    Args:
    - var (`Any`): Variable to check if it is None.
    - de (`Any`): Default value to return if var is None.

    Returns:
    `Any`: `var` if `var` is not None else `de`.
    """
    if var is None:
        return de
    return var
