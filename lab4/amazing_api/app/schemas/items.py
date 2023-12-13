from abc import ABC, abstractmethod
from pydantic import BaseModel


class ItemBase(BaseModel, ABC):
    weight: float
    count: int
    container_id: int
    type: str
    specific_attribute: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    item_id: int

    class Config:
        orm_mode = True