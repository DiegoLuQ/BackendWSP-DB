from fastapi import APIRouter, Depends
#DB
from sqlalchemy.orm import Session
from core.db.session import get_db
#REPOSITORY
from core.db.repository.repo_user import add_chat_number
#SCHEMAS
from core.schemas.schema_user import Schema_UserWSP
#MODELS
from core.db.models.models_user import Model_WSP_User

router = APIRouter()

@router.get("/")
async def home():
    return {"Hola":"World"}


@router.post("/register_user")
async def post_register_user(model:Model_WSP_User, db:Session):
    data = await add_chat_number(chat_user=model, db=db)
    return data

