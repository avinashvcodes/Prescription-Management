from sqlalchemy import Column,String,ForeignKey
from sqlalchemy.dialects.postgresql import UUID,JSONB,DOUBLE_PRECISION,TIMESTAMP
from sqlalchemy.orm import relationship
from models.base import BaseModel
from uuid import uuid4

class Physicians(BaseModel):

    """
    Class for mapping physicians table in database
    """

    __tablename__ = "physicians"

    physician_id = Column(UUID(as_uuid=True),primary_key = True,nullable = False,default = uuid4)
    name = Column(String(60),nullable = False)
    qualification = Column(JSONB,nullable = False)
    grade = Column(String(60),nullable = False)
    specialisation = Column(JSONB,nullable = False)
    year_of_experience = Column(DOUBLE_PRECISION,nullable = False)
    address_id = Column(UUID(as_uuid=True),ForeignKey("address.address_id"),nullable = False)
    other_details = Column(JSONB)
    created_by = Column(String(120),nullable = False)
    created_on = Column(TIMESTAMP,nullable = False)
    updated_by = Column(String(120),nullable = False)
    updated_on = Column(TIMESTAMP,nullable = False)

    prescriptions_physicians_details = relationship(
        "Prescriptions",
        back_populates = "physicians_details"
    )

    address_details = relationship(
        "Address",
        back_populates = "physicians_address_details"
    )

    def get_physician(self):

        """
        Title:
            get_physician method of Physician Class
        Args:
            self: Reference to the instance or current object of the class.
        Returns:
            physician details as Dictionary.
        """

        response = {
            "physiciansId" : str(self.physician_id),
            "address" : self.address_details.get_address(),
            "name" : self.name,
            "qualification" : self.qualification,
            "grade" : self.grade,
            "specialisation" : self.specialisation,
            "yearsOfExperience" : self.year_of_experience,
            "otherDetails" : self.other_details
        }

        return response