from sqlalchemy import Column,String,ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP, JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from datetime import datetime
from .prescriptions_mapping import PrescriptionsMapping
from models.base import BaseModel

class Prescriptions(BaseModel):

    """
    Class for mapping of prescription table in database
    """

    __tablename__ = "prescriptions"

    prescription_id = Column(UUID(as_uuid=True),primary_key=True,nullable=False,server_default = func.gen_random_uuid())
    customer_id = Column(UUID(as_uuid=True),ForeignKey("customer.customer_id"),nullable = False)
    physicians_id = Column(UUID(as_uuid=True),ForeignKey("physicians.physician_id"),nullable = False)
    status = Column(String(1),nullable = False)
    payment_method_code = Column(String(3),ForeignKey("payment_method.code"),nullable = False) 
    date = Column(TIMESTAMP,nullable = False)
    other_details = Column(JSONB)
    created_by = Column(String(120),nullable = False)
    created_on = Column(TIMESTAMP,nullable = False,server_default = func.now()) 
    updated_by = Column(String(120),nullable = False)
    updated_on = Column(TIMESTAMP,nullable = False,server_default = func.now()) 

    customer_details = relationship(
        "Customer",
        back_populates = "prescriptions_customer_details"
    )

    physicians_details = relationship(
        "Physicians",
        back_populates = "prescriptions_physicians_details"
    )

    prescription_items_details = relationship(
        "PrescriptionsItems",
        back_populates = "prescription_detail"
    )

    payment_details = relationship(
        "PaymentMethod",
        back_populates = "prescriptions_payment_details"
    )

    def create_prescription(self,payload):

        """
        Title:
            create_prescription method of Prescription Class
        Args:
            self: Reference to the instance or current object of the class.
            payload: input dictionary.
        Returns:
            None. Sets attributes for current object
        """

        pmap = PrescriptionsMapping.PRESCRIPTIONS_MAPPING_TEMPLATE
        for key in payload:
            if key in pmap:
                a = pmap[key]
                setattr(self,a,payload[key])
        if "date" in payload:
            setattr(self,"date",datetime.strptime(payload["date"],'%d-%m-%Y'))
        
        if "paymentMethod" in payload:
            setattr(self,"payment_method_code",payload["paymentMethod"]["code"])

        if "createdBy" in payload:
            setattr(self,"updated_by",payload["createdBy"])

    def update_prescription(payload):

        """
        Title:
            update_prescription method of Prescription Class
        Args:
            payload: input dictionary.
        Returns:
            Dictionary with values to update
        """

        response = {}
        pmap = PrescriptionsMapping.PRESCRIPTIONS_MAPPING_TEMPLATE
        for key in payload:
            if key in pmap:
                a = pmap[key]
                response[a] = payload[key]
        if "date" in payload:
            response["date"] = datetime.strptime(payload["date"],'%d-%m-%Y')
        
        if "paymentMethod" in payload:
            response["payment_method_code"] = payload["paymentMethod"]["code"]
        
        response["updated_on"] = datetime.now()
        return response
    
    def get_prescription(self):

        """
        Title:
            get_prescription method of Prescription Class
        Args:
            self: Reference to the instance or current object of the class.
        Returns:
            Details of Prescription as Dictionary
        """

        prescription_items_array = []
        for i in self.prescription_items_details:
            prescription_items_array.append(i.get_prescriptions_items())
        response = {
            "prescriptionId" : str(self.prescription_id),
            "prescriptionItems" : prescription_items_array,
            "physiciansId" : str(self.physicians_id),
            "physician" : self.physicians_details.get_physician(),
            "customerId" : str(self.customer_id),
            "customer" : self.customer_details.get_customer(),
            "status" : self.status,
            "paymentMethod" : self.payment_details.get_payment_method(),
            "otherDetails" : self.other_details,
            "date" : self.date.strftime("%d-%m-%Y %H:%M:%S"),
            "createdBy" : self.created_by,
            "createdOn" : self.created_on.date().strftime("%d-%m-%Y"),
            "updatedBy" : self.updated_by,
            "updatedOn" : self.updated_on.strftime("%d-%m-%Y")
        }

        return response