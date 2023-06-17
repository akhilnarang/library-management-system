from app.models.member import Member
from app.schemas.member import MemberCreate, MemberUpdate
from .base import CRUDBase


class CRUDMember(CRUDBase[Member, MemberCreate, MemberUpdate]):
    pass


member = CRUDMember(Member)
