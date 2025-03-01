from os import getenv
from sqlmodel import create_engine, Session
from model import SQLModel

url = "{}://{}:{}@{}:{}/{}".format(
    getenv('DB_CONNECTOR'),
    getenv('DB_USER'),
    getenv('DB_PASSWORD'),
    getenv('DB_HOST'),
    getenv('DB_PORT'),
    getenv('DB_DATABASE')
)
engine = create_engine(url)
SQLModel.metadata.create_all(engine)

class Connection:
    def __enter__(self):
        self.session = Session(engine)
        return self.session

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()
        return False
