from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from IoTDashboard.settings import APP_ENV, DB_URL

engine = create_engine(
    url=DB_URL,
    echo=False if APP_ENV == "PRODUCTION" else True,
    pool_pre_ping=True,  # https://stackoverflow.com/a/55127866
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def get_db_manager():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
