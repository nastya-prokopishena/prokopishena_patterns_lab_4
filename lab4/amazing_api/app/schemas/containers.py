from abc import ABC, abstractmethod
from pydantic import BaseModel


class ContainerBase(BaseModel, ABC):
    weight: int
    type: str
    item_ids: str


class ContainerCreate(ContainerBase):
    pass


class Container(ContainerBase):
    container_id: int

    class Config:
        orm_mode = True