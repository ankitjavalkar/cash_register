import csv

from config import CATALOGUE, DELIVERY, OFFERS


class IncorrectProductCodeException(Exception)
    pass

class Register():
    def __init__(catalogue, delivery, offers):
        self.catalogue = catalogue
        self.delivery = delivery
        self.offers = offers
        self.cart = []

    def add_product(self, prod_code):
        if prod_code in self.catalogue:
            self.cart.append(prod_code)
        else:
            raise IncorrectProductCodeException(
                'Incorrect product code | Product does not exist'
            )

    def calc_total(self):

