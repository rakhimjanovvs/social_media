from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PostSchema(BaseModel):
    title: str
    main_text: str
    uid: int
    reg_date: datetime


class PostRead(BaseModel):
    status: int
    message: bool