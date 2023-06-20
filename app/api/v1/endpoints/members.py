from fastapi import APIRouter

from app import crud, schemas
from app.api.annotations import DB
from app.exceptions import ConflictException, NotFoundException

router = APIRouter()


@router.get("/")
def get_members(db: DB, skip: int = 0, limit: int = 100) -> list[schemas.Member]:
    """
    An endpoint that returns a given count of members from the database.
    """
    return [schemas.Member.from_orm(member) for member in crud.member.get_multi(db, skip=skip, limit=limit)]


@router.post("/")
def create_member(db: DB, member_create: schemas.MemberCreate) -> schemas.Member:
    """
    An endpoint that creates a member in the database.
    """
    if crud.member.get_by_email(db, email=member_create.email):
        raise ConflictException(
            detail="Someone with this email already exists!",
        )
    return schemas.Member.from_orm(crud.member.create(db, obj_in=member_create))


@router.get("/{member_id}")
def get_member(db: DB, member_id: int) -> schemas.Member:
    """
    An endpoint that returns a member from the database.
    """
    return schemas.Member.from_orm(crud.member.get(db, id=member_id))


@router.put("/{member_id}")
def update_member(db: DB, member_id: int, member_update: schemas.MemberUpdate) -> schemas.Member:
    """
    An endpoint that updates a member in the database.
    """
    if member := crud.member.get(db, id=member_id):
        return schemas.Member.from_orm(crud.member.update(db, db_obj=member, obj_in=member_update))
    raise NotFoundException(detail="The requested member does not exist!")


@router.delete("/{member_id}")
def delete_member(db: DB, member_id: int) -> schemas.Member:
    """
    An endpoint that deletes a member from the database.
    """
    return schemas.Member.from_orm(crud.member.remove(db, id=member_id))
