from sqlalchemy import Column,String,ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP, JSONB, DATE
from models.base import BaseModel
from sqlalchemy.orm import relationship
from uuid import uuid4


class Customer(BaseModel):

    """
    Class for mapping of customer table in database
    """

    __tablename__ = "customer"

    customer_id = Column(UUID(as_uuid=True),primary_key = True,nullable = False,default = uuid4)
    address_id = Column(UUID(as_uuid=True),ForeignKey("address.address_id"),nullable = False)
    first_name = Column(String(60),nullable = False)
    last_name = Column(String(60))
    gender = Column(String(1),nullable = False)
    phone = Column(String(60))
    mobile = Column(String(60),nullable = False)
    email = Column(String(60),nullable = False)
    date_of_birth = Column(DATE,nullable = False)
    credit_card_number = Column(String(50))
    expiry_date = Column(DATE)
    other_details = Column(JSONB)
    created_by = Column(String(120),nullable = False)
    created_on = Column(TIMESTAMP,nullable = False)
    updated_by = Column(String(120),nullable = False)
    updated_on = Column(TIMESTAMP,nullable = False)

    prescriptions_customer_details = relationship(
        "Prescriptions",
        back_populates = "customer_details"
    )

    address_details = relationship(
        "Address",
        back_populates = "customer_address_details"
    )

    def get_customer(self):

        """
        Title:
            get_customer method of Customer Class
        Args:
            self: Reference to the instance or current object of the class.
        Returns:
            Customer details as Dictionary.
        """

        response = {
            "customerId" : str(self.customer_id),
            "address" : self.address_details.get_address(),
            "firstName" : self.first_name,
            "lastName" : self.last_name,
            "gender" : self.gender,
            "phone" : self.phone,
            "mobile" : self.mobile,
            "email" : self.email,
            "dateOfBirth" : self.date_of_birth.strftime("%d-%m-%Y"),
            "cerditCardNumber" : self.credit_card_number,
            "expiryDate" : self.expiry_date.strftime("%m-%y"),
            "otherDetails" : self.other_details
        }

        return response