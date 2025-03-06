from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP, UUID
from sqlalchemy.orm import relationship
from models.base import BaseModel
from uuid import uuid4

class Address(BaseModel):

    """
    Class for mapping address table in database
    """

    __tablename__ = "address"

    address_id = Column(UUID(as_uuid=True),primary_key = True,nullable = False,default = uuid4)
    door_no = Column(String(30),nullable = False) 
    address_line_1 = Column(String(60),nullable = False)
    address_line_2 = Column(String(60))
    place = Column(String(30),nullable = False)
    city = Column(String(50),nullable = False)
    zipcode = Column(Integer,nullable = False)
    latitude = Column(String(30))
    longitude = Column(String(30))
    country_code = Column(UUID(as_uuid=True),ForeignKey("country.country_uuid"),nullable = False)
    other_details = Column(JSONB)
    created_by = Column(String(120),nullable = False)
    created_on = Column(TIMESTAMP,nullable = False)
    updated_by = Column(String(120),nullable = False)
    updated_on = Column(TIMESTAMP,nullable = False)

    company_address_details = relationship(
        "DrugCompanies",
        back_populates = "address_details"
    )

    country_details = relationship(
        "Country",
        back_populates = "country_address_details"
    )

    physicians_address_details = relationship(
        "Physicians",
        back_populates = "address_details"
    )

    customer_address_details = relationship(
        "Customer",
        back_populates = "address_details"
    )

    def get_address(self):

        """
        Title:
            get_address method of Address Class
        Args:
            self: Reference to the instance or current object of the class.
        Returns:
            Address details as Dictionary.
        """

        response = {
            "addressId" : str(self.address_id),
            "doorNo" : self.door_no,
            "addressLine1" : self.address_line_1,
            "addressLine2" : self.address_line_2,
            "place" : self.place,
            "city" : self.city,
            "zipcode" : self.zipcode,
            "latitude" : self.latitude,
            "longitude" : self.longitude,
            "countryCodeUuid" : str(self.country_details.country_uuid),
            "countryCode" : self.country_details.country_code,
            "countryName" : self.country_details.country_name,
            "otherDetails" : self.other_details
        }
        return response