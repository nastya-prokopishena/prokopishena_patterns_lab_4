from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy.future import select

from app.models.models import Ship
from app.schemas.ship import IShip


class ShipRepository:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create_ship(self, ship: IShip) -> Ship:
        db_ship = Ship(**ship.dict())
        self.db_session.add(db_ship)
        self.db_session.commit()
        self.db_session.refresh(db_ship)
        return db_ship

    def get_ship_by_id(self, ship_id: int) -> Ship:
        ship = self.db_session.execute(
            select(Ship).filter(Ship.id == ship_id)
        )
        return ship.scalars().first()

    def get_ships(self):
        ships = self.db_session.execute(select(Ship).order_by(Ship.id))
        return ships.scalars().all()

    def update_ship(self, ship_id: int, ship: IShip) -> Ship:
        ship_update = update(Ship).where(
            Ship.id == ship_id
        ).values(**ship.dict(exclude_unset=True))
        ship_update.execution_options(
            synchronize_session="fetch"
        )
        self.db_session.execute(ship_update)
        return

    def delete_ship(self, ship_id: int) -> Ship:
        ship = self.get_ship_by_id(ship_id)
        self.db_session.delete(ship)
        self.db_session.commit()
        return ship
