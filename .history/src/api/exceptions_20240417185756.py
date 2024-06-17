def c_exc_str(cls):
    cls.__str__ = lambda self: self.message
    return cls


def c_exc(cls):
    if cls.__mro__[-2] is BaseException:
        exc = cls.__mro__[1]
    else:
        exc = Exception

    def __init__(self, message: str) -> None:
        self.message = message
        exc.__init__(self, message)

    cls.__init__ = __init__
    return c_exc_str(cls)


@c_exc_str
class CDiTypeError(TypeError):
    def __init__(self, og_path: str, idx: int, type: type) -> None:
        if type is list:
            conc = ", but is not the last element of the path."
        else:
            conc = (
                ", expected dictionary or list, if the list is the value of the "
                "last element in the path."
            )
        self.message = (
            f'`{"/".join(og_path.split("/")[:idx + 1])}` is a ' + type.__name__ + conc
        )
        super().__init__(self.message)


@c_exc
class CDKeyError(KeyError):
    pass


@c_exc
class CDTypeError(TypeError):
    pass
