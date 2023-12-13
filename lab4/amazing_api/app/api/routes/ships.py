from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.ship import IShip
from app.db.database import get_db
from app.db.repositories.ships import ShipRepository
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=IShip, status_code=status.HTTP_201_CREATED)
def create_ship(ship: IShip, db: Session = Depends(get_db)):
    ship_crud = ShipRepository(db_session=db)
    db_ship = ship_crud.get_ship_by_id(ship_id=ship.id)
    if db_ship:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ship already exists"
        )
    db_ship = ship_crud.create_ship(ship=ship)
    return db_ship


@router.get("/", response_model=list[IShip], status_code=status.HTTP_200_OK)
def get_all_ships(db: Session = Depends(get_db)):
    ship_crud = ShipRepository(db_session=db)
    return ship_crud.get_ships()
