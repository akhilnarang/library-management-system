from sqlalchemy import column
from sqlalchemy.orm import Session

from app.models.member import Member
from app.schemas.member import MemberCreate, MemberUpdate

from .base import CRUDBase


class CRUDMember(CRUDBase[Member, MemberCreate, MemberUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Member | None:
        return db.query(self.model).where(column("email") == email).first()


member = CRUDMember(Member)
