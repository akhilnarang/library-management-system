import logging
from typing import Any, Generic, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.base_class import Base
from app.exceptions import BadRequestException

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id: int) -> ModelType | None:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
        self,
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
        filters: list | None = None,
    ) -> list[ModelType]:
        if filters is None:
            filters = []
        return db.query(self.model).filter(*filters).offset(skip).limit(limit).all()

    def create(
        self, db: Session, *, obj_in: CreateSchemaType, commit: bool = True
    ) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        try:
            # Just flush if we don't want to commit here
            if commit:
                db.commit()
            else:
                db.flush()
        except Exception as e:
            logging.error("Failed to create object", e.__str__())
            db.rollback()
            raise e
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: UpdateSchemaType | dict[str, Any],
        commit: bool = True,
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        try:
            # Just flush if we don't want to commit here
            if commit:
                db.commit()
            else:
                db.flush()
        except Exception as e:
            logging.error("Failed to update object", e.__str__())
            db.rollback()
            raise e
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int, commit: bool = True) -> ModelType:
        if obj := db.query(self.model).get(id):
            db.delete(obj)
            try:
                # Just flush if we don't want to commit here
                if commit:
                    db.commit()
                else:
                    db.flush()
                return obj
            except Exception as e:
                logging.error("Failed to delete object", e.__str__())
                db.rollback()
                raise e
        logging.error(f"Failed to delete object {id=}")
        raise BadRequestException("Object not found")

    def commit(self, db: Session) -> None:
        try:
            db.commit()
        except Exception as e:
            logging.error("Failed to commit transaction", e.__str__())
            raise e

    def rollback(self, db: Session) -> None:
        db.rollback()
