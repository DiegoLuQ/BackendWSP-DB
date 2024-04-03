from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

# sqlalchemy_database_url = environ.get("MYSQL_URL")
sqlalchemy_database_url = "mysql+pymysql://root@localhost:33306/wsp-db"
# sqlalchemy_database_url = "mysql+pymysql://root@localhost:3306/prueba"

# "mysql+pymysql://root@localhost:3306/prueba"
engine = create_engine(sqlalchemy_database_url)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        