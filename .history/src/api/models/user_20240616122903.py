import bcrypt
from pydantic import BaseModel, EmailStr, Field

import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class UserReg(BaseModel):
    email: EmailStr = Field(
        title="email",
        description="Allowed email address",
    )
    username: str = Field(
        title="username",
        min_length=1,
        max_length=32,
        description="Allowed length from 1 to 32.",
    )
    password: str = Field(
        title="password",
        min_length=6,
        max_length=32,
        description="Allowed length from 6 to 32.",
    )
    confirm_password: str = Field(
        title="password",
        min_length=6,
        max_length=32,
        description="Allowed length from 6 to 32.",
    )


class User(BaseModel):
    username: str = Field(
        title="username",
        min_length=1,
        max_length=32,
        description="Allowed length from 1 to 32.",
    )
    password: str = Field(
        title="password",
        min_length=6,
        max_length=32,
        description="Allowed length from 6 to 32.",
    )


def hash_pw(pw: str):
    return bcrypt.hashpw(pw.encode("utf-8"), bcrypt.gensalt(12))


def comp_pw(pw: str, hash: str):
    return bcrypt.checkpw(pw.encode("utf-8"), hash.encode("utf-8"))
