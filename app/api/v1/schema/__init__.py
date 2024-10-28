from typing import List, Optional

from base_cms import BaseModel


class BookQuerySearchSchema(BaseModel):
    q: Optional[str] = str()


class BookInSchema(BaseModel):
    title: str
    author: str
    image: str
    summary: str


class BookOutSchema(BaseModel):
    id: int
    title: str
    author: str
    image: str
    summary: str


class BookSchemaList(BaseModel):
    __root__: List[BookOutSchema]
