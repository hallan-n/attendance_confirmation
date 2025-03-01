from sqlmodel import create_engine, Session
from model import SQLModel

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)


class Connection:
    def __enter__(self):
        self.session = Session(engine)
        return self.session

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()
        return False
