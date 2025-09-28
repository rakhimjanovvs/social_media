from pydantic import BaseModel
from typing import Optional


class CommentSchema(BaseModel):
    text: str
    uid: int
    pid: int
    reg_date: datetime


class CommentRead(BaseModel):
    status: int
    message: bool