from os import getenv
from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy.pool import QueuePool


class Connection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_db()
        return cls._instance

    def _init_db(self):
        env = getenv("ENVIRONMENT", "development")

        if env == "production":
            self.database_url = "{}://{}:{}@{}:{}/{}".format(
                getenv("DB_CONNECTOR"),
                getenv("DB_USER"),
                getenv("DB_PASSWORD"),
                getenv("DB_HOST"),
                getenv("DB_PORT"),
                getenv("DB_DATABASE"),
            )
            self.engine = create_engine(
                self.database_url, poolclass=QueuePool, pool_size=10, max_overflow=20
            )
        else:
            self.database_url = "sqlite:///database.db"
            self.engine = create_engine(
                self.database_url, connect_args={"check_same_thread": False}
            )

        SQLModel.metadata.create_all(self.engine)

    def __enter__(self):
        self.session = Session(self.engine)
        return self.session

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()
        return False
