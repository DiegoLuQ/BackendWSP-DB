from sqlalchemy import Column, Integer, String, Date, Text
from core.db.base_class import Base

class Model_UserWSP(Base):
    __tablename__ = "wsp_pedido"
    id = Column(Integer, primary_key=True,autoincrement=True)
    number = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
