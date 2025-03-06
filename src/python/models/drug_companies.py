from sqlalchemy import Column,String,ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP, JSONB, NUMERIC
from models.base import BaseModel
from sqlalchemy.orm import relationship
from uuid import uuid4

class DrugCompanies(BaseModel):

    """
    Class for mapping drug_companies table in database
    """

    __tablename__ = "drug_companies"

    company_id = Column(UUID(as_uuid=True),primary_key = True,nullable = False,default = uuid4)
    company_name = Column(String,nullable = False)
    company_age = Column(NUMERIC,nullable = False)
    specialization = Column(JSONB,nullable = False)
    address_id = Column(UUID,ForeignKey("address.address_id"),nullable = False)
    other_details = Column(JSONB)
    created_by = Column(String(120),nullable = False)
    created_on = Column(TIMESTAMP,nullable = False)
    updated_by = Column(String(120),nullable = False)
    updated_on = Column(TIMESTAMP,nullable = False)

    drug_company_details = relationship(
        "Drugs",
        back_populates = "company_details"
    )

    address_details = relationship(
        "Address",
        back_populates = "company_address_details"
    )

    def get_company(self):

        """
        Title:
            get_company method of DrugCompany Class
        Args:
            self: Reference to the instance or current object of the class.
        Returns:
            DrugCompany details as Dictionary.
        """

        response = {
            "companyId" : str(self.company_id),
            "address" : self.address_details.get_address(),
            "companyName" : self.company_name,
            "companyAge" : self.company_age,
            "specialisation" : self.specialization,
            "otherDetails" : self.other_details
        }

        return response

    