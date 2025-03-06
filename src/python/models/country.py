from sqlalchemy import Column,String
from sqlalchemy.dialects.postgresql import UUID
from models.base import BaseModel
from sqlalchemy.orm import relationship
from uuid import uuid4


class Country(BaseModel):

    """
    Class for mapping the country table in database
    """

    __tablename__ = "country"

    country_uuid = Column(UUID(as_uuid=True),primary_key=True,nullable=False,default = uuid4)
    country_code = Column(String(2),nullable=False)
    country_name = Column(String(60),nullable=False)

    country_address_details = relationship(
        "Address",
        back_populates = "country_details"
    )

