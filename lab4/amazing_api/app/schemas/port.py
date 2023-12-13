from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING
import haversine as hs
from pydantic import BaseModel


class IPort(BaseModel, ABC):
    id: int



    class Config:
        orm_mode = True


class Port(IPort):
    latitude: float
    longitude: float
    title: str
    items: List['Item'] = []
    containers: List['Container'] = []
    ship_history: List[int] = []
    current_ships: List[int] = []

    def get_distance(self, port) -> float:
        dist = hs.haversine((self.latitude, self.longitude), (port.latitude, port.longitude))
        return dist
