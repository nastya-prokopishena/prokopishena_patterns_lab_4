from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import List, TYPE_CHECKING

from app.schemas.port import Port
from app.schemas.containers import Container
from app.schemas.items import Item


class IShip(BaseModel, ABC):
    total_weight_capacity: int
    max_number_of_all_containers: int
    max_number_of_heavy_containers: int
    max_number_of_refrigerated_containers: int
    max_number_of_liquid_containers: int
    fuel_consumption_per_km: float
    port_id: int
    id: int

    def sail_to(self, port) -> bool:
        pass

    def refuel(self, amount_of_fuel: float) -> None:
        pass

    def load(self, container) -> bool:
        pass

    def unload(self, container) -> bool:
        pass

    class Config:
        orm_mode = True


class Ship(IShip):
    port: 'Port'
    destination_port: 'Port'
    fuel: float
    containers: List['Container']
    items: List['Item']
    ship_counter: int = 1
    weight: str

    def sail_to(self, port: 'Port') -> bool:
        if self.fuel > 0 and isinstance(self.port, Port) and isinstance(port, Port):
            distance = self.port.get_distance(port)
            fuel_required = distance * self.fuel_consumption_per_km
            if self.fuel >= fuel_required:
                self.fuel -= fuel_required
                if self.port.outgoing_ship(self) and port.incoming_ship(self):
                    self.destination_port = port
                    return True
        return False

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel += amount_of_fuel

    def load(self, container: 'Container') -> bool:
        if len(self.containers) < self.max_number_of_all_containers:
            self.containers.append(container)
            return True
        return False

    def unload(self, container: 'Container') -> bool:
        if container in self.containers:
            self.containers.remove(container)
            return True
        return False
