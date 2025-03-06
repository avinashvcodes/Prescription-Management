from sqlalchemy import Column,String,ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP, JSONB, NUMERIC
from models.base import BaseModel
from sqlalchemy.orm import relationship
from uuid import uuid4

class Drugs(BaseModel):

    """
    Class for mapping of drugs table in database
    """

    __tablename__ = "drugs"

    drug_id = Column(UUID(as_uuid=True),nullable = False,primary_key = True)
    company_id = Column(UUID(as_uuid=True),ForeignKey("drug_companies.company_id"),nullable = False)
    drug_name = Column(String(100),nullable = False)
    drug_cost = Column(NUMERIC(10,2),nullable = False)
    quantity = Column(NUMERIC(10,0),nullable = False)
    manufacturer_date = Column(TIMESTAMP,nullable = False)
    expiry_date = Column(TIMESTAMP,nullable = False)
    packing_type = Column(String(20))
    other_details = Column(JSONB)
    created_by = Column(String(120),nullable = False)
    created_on = Column(TIMESTAMP,nullable = False)
    updated_by = Column(String(120),nullable = False)
    updated_on = Column(TIMESTAMP,nullable = False)

    prescription_item_drug_detail = relationship(
        "PrescriptionsItems",
        back_populates = "drug_detail"
    )

    company_details = relationship(
        "DrugCompanies",
        back_populates = "drug_company_details"
    )

    def get_drug(self):

        """
        Title:
            get_drug method of Drugs Class
        Args:
            self: Reference to the instance or current object of the class.
        Returns:
            Drug details as Dictionary.
        """

        response = {
            "drugId" : str(self.drug_id),
            "company" : self.company_details.get_company(),
            "drugName" : self.drug_name,
            "drugCost" : self.drug_cost,
            "manufacturerDate" : self.manufacturer_date.strftime("%d-%m-%Y"),
            "expiryDate" : self.expiry_date.strftime("%d-%m-%Y"),
            "packingType" : self.packing_type,
            "otherDetails" : self.other_details
        }

        return response
