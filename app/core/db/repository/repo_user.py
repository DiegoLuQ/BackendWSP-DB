from sqlalchemy.orm import Session
from core.db.models.models_user import Model_UserWSP
from core.schemas.schema_user import Schema_UserWSP


async def add_chat_number(chat_user:Model_UserWSP, db:Session):
    model = Model_UserWSP(**chat_user.dict())
    db.add(model)
    db.commit()
    db.refresh(model)
    return model