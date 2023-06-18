from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.api import deps

DB = Annotated[Session, Depends(deps.get_db)]
