"""This file should have our order classes in it."""

#import random from choice or import random

class AbstractMelonOrder(object):
    """Class to serve as base class and refractor"""
    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        # order_type = "to do later by calling the method in either DomesticMelonOrder or InternationalMelonOrder"
        
    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        if self.species == "Christmas Melon":
            return base_price * 1.5
        if self.qty < 10 and self.order_type == "international":
            return total + 3
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_base_price(self):

        splurge_pricing = randint(5,9)
        self.get_total
        #



class GovernmentMelonOrder(AbstractMelonOrder):
    """A US government melon order"""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""
        super(GovernmentMelonOrder, self).__init__(species, qty, "domestic", 0.00)
        
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed

 
class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic" , 0.08)
        


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)
    
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
