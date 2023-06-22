from fastapi import APIRouter

from app import crud, schemas
from app.api.annotations import DB

router = APIRouter()


@router.get("/")
def get_transactions(db: DB) -> list[schemas.Transaction]:
    """
    An endpoint that returns a given count of transactions from the database.
    """
    return [schemas.Transaction.from_orm(transaction) for transaction in crud.transaction.get_multi(db)]
