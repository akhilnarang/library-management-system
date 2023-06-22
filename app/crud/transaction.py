from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionUpdate

from .base import CRUDBase


class CRUDTransaction(CRUDBase[Transaction, TransactionCreate, TransactionUpdate]):
    pass


transaction = CRUDTransaction(Transaction)
