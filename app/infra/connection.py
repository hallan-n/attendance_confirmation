from os import getenv
from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy.pool import QueuePool
import logging


class Connection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_db()
        return cls._instance

    def _validate_env_vars(self):
        required_vars = [
            "DB_CONNECTOR",
            "DB_USER",
            "DB_PASSWORD",
            "DB_HOST",
            "DB_PORT",
            "DB_DATABASE",
        ]
        for var in required_vars:
            if not getenv(var):
                raise ValueError(f"A variável de ambiente {var} não está configurada.")

    def _get_database_url(self):
        if getenv("ENVIRONMENT") == "production":
            return "{}://{}:{}@{}:{}/{}".format(
                getenv("DB_CONNECTOR"),
                getenv("DB_USER"),
                getenv("DB_PASSWORD"),
                getenv("DB_HOST"),
                getenv("DB_PORT"),
                getenv("DB_DATABASE"),
            )
        return "sqlite:///database.db"

    def _init_db(self):
        try:
            logging.info("Inicializando o banco de dados...")
            env = getenv("ENVIRONMENT")
            if env == "production":
                self._validate_env_vars()
            self.database_url = self._get_database_url()
            if env == "production":
                self.engine = create_engine(
                    self.database_url,
                    poolclass=QueuePool,
                    pool_size=10,
                    max_overflow=20,
                )
            else:
                self.engine = create_engine(
                    self.database_url, connect_args={"check_same_thread": False}
                )
            SQLModel.metadata.create_all(self.engine)
            logging.info(f"Banco de dados conectado: {self.database_url}")
        except Exception as e:
            logging.error(f"Erro ao inicializar o banco de dados: {str(e)}")
            raise

    def __enter__(self):
        self.session = Session(self.engine)
        return self.session

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()
        return False

    def get_session(self):
        return Session(self.engine)
