from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BaseModel(Base):

    """
    An abstract class inherits Base class
    """
    
    __abstract__ = True