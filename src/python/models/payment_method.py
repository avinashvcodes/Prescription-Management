from sqlalchemy import Column,String
from sqlalchemy.orm import relationship
from models.base import BaseModel

class PaymentMethod(BaseModel):

    """
    Class for mapping of payment_method table in database
    """

    __tablename__ = "payment_method"

    code = Column(String(3),primary_key = True,nullable = False)
    name = Column(String(30),nullable = False)
    description = Column(String(300))

    prescriptions_payment_details = relationship(
        "Prescriptions",
        back_populates = "payment_details"
    )

    def get_payment_method(self):

        """
        Title:
            get_payment_method method of PaymentMethod Class
        Args:
            self: Reference to the instance or current object of the class.
        Returns:
            payment method details as Dictionary.
        """

        response = {
            "code" : self.code,
            "name" : self.name,
            "description" : self.description
        }

        return response