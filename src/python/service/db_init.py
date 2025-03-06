from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

class Connect:

    """
    Class that has method for connecting to database
    """
    
    def __init__(self):
        self.username = os.environ["username"]
        self.password = os.environ["password"]
        self.host = os.environ["host"]
        self.port = os.environ["port"]
        self.database = os.environ["database"]
        self.timeout = os.environ["timeout"]
        self.schema = os.environ["schema"]

    def connect(self):

        """
        Title:
            connect method of Connect class
        Args:
            self: Reference to current object or instance
        Returns:
            session.
        """

        connection_string = f"postgresql+psycopg2://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        connect_args={
                'connect_timeout': self.timeout,
                'options': f'-csearch_path={self.schema}'
            }
        engine = create_engine(connection_string,connect_args = connect_args)
        Session = sessionmaker(bind = engine)
        return Session


