from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from models.base import BaseModel
from datetime import datetime
from .prescriptions_items_mapping import PrescriptionsItemsMapping
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class PrescriptionsItems(BaseModel):

    """
    Class for mapping of prescription_items table in database
    """

    __tablename__ = "prescriptions_items"

    prescription_id = Column(UUID(as_uuid=True),ForeignKey("prescriptions.prescription_id"),primary_key = True,nullable = False)
    drug_id = Column(UUID(as_uuid=True),ForeignKey("drugs.drug_id"),primary_key = True,nullable = False)
    quantity = Column(Integer,nullable = False)
    instruction_to_customer = Column(String(300))
    created_by = Column(String(120),nullable = False)
    created_on = Column(TIMESTAMP,nullable = False,server_default = func.now())
    updated_by = Column(String(120),nullable = False)
    updated_on = Column(TIMESTAMP,nullable = False,server_default = func.now())

    prescription_detail = relationship(
        "Prescriptions",
        back_populates = "prescription_items_details"
    )

    drug_detail = relationship(
        "Drugs",
        back_populates = "prescription_item_drug_detail"
    )

    def create_prescriptions_items(self,payload):

        """
        Title:
            create_prescriptions_items method of PrescriptionItems Class
        Args:
            self: Reference to the instance or current object of the class.
            payload: input dictionary.
        Returns:
            None. Set attribute value to self
        """

        pimap = PrescriptionsItemsMapping.PRESCRIPTIONS_ITEMS_MAPPING
        for key in payload:
            if key in pimap:
                a = pimap[key]
                setattr(self,a,payload[key])
        if "createdBy" in payload:
            setattr(self,"updated_by",payload["createdBy"])
    
    def update_prescriptions_items(payload):

        """
        Title:
            update_prescriptions_items method of PrescriptionItems Class
        Args:
            payload: input dictionary.
        Returns:
            Dictionary of values to update
        """

        response = {}
        pimap = PrescriptionsItemsMapping.PRESCRIPTIONS_ITEMS_MAPPING
        for key in payload:
            if key in pimap and key != "prescriptionId" and key != "drugId":
                a = pimap[key]
                response[a] = payload[key]
        
        response["updated_on"] = datetime.now()
        return response

    def get_prescriptions_items(self):

        """
        Title:
            get_prescriptions_items method of PrescriptionItems Class
        Args:
            self: Reference to the instance or current object of the class.
        Returns:
            Details of Prescription Items as Dictionary
        """

        response = {
            "drugId" : str(self.drug_id),
            "prescriptionId" : str(self.prescription_id),
            "quantity" : self.quantity,
            "instructionToCustomer" : self.instruction_to_customer,
            "drug" : self.drug_detail.get_drug()
        }

        return response
    
    def get_prescriptionsitems(self):

        """
        Title:
            get_prescriptionsitems method of PrescriptionItems Class
        Args:
            self: Reference to the instance or current object of the class.
        Returns:
            Details of Prescription Items as Dictionary
        """

        response = {
            "drugId" : str(self.drug_id),
            "prescriptionId" : str(self.prescription_id),
            "quantity" : self.quantity,
            "instructionToCustomer" : self.instruction_to_customer,
            "drug" : self.drug_detail.get_drug(),
            "createdBy" : self.created_by,
            "createdOn" : self.created_on.strftime("%d-%m-%Y"),
            "updatedBy" : self.updated_by,
            "updatedOn" : self.updated_on.strftime("%d-%m-%Y")
        }

        return response