import csv

from config import CATALOGUE, DELIVERY, OFFERS


class IncorrectProductCodeException(Exception):
    pass

class EmptyCartException(Exception):
    pass


class Register():
    def __init__(self, catalogue, delivery, offers):
        self.catalogue = catalogue
        self.delivery = delivery
        self.offers = offers
        self.cart = []
        self.total = 0.0

    def add_product(self, prod_code):
        if prod_code in self.catalogue:
            self.cart.append(prod_code)
        else:
            raise IncorrectProductCodeException(
                'Incorrect product code {0} | Product does not exist'.format(
                    prod_code
                )
            )

    def match_offer(self, offer):
        cursor = 0
        for ix, i in enumerate(self.cart):
            ix_list = []
            if i == offer.pattern[cursor]:
                cursor += 1
                ix_list.append(ix)
                if cursor == len(offer):
                    self.total += offer.amt
                    return ix_list
            else:
                cursor = 0

    def calc_non_offer_total(self):
        for prod_code in self.cart:
            self.total += self.catalogue[prod_code][1]

    def calc_delivery_charges(self):
        for lower_bound, upper_bound, charges in self.delivery:
            if lower_bound <= self.total < upper_bound:
                self.total += charges
                break

    def calc_total(self):
        if self.cart:
            for offer in self.offers:
                found_match_indices = self.match_offer(offer)
                if found_match_indices:
                    for ix in sorted(found_match, reverse=True):
                        self.cart.pop(ix)

            self.calc_non_offer_total()
            self.calc_delivery_charges()
        else:
            raise EmptyCartException(
                'Product buy cart is empty | Add product codes'
            )

if __name__=='__main__':
    help_txt = (
            'Usage: python3 cash_register.py [OPTIONS]...',
            '\n a, add [PRODUCT-CODE1] [PRODUCT-CODE2] [PRODUCT-CODE3]...',
            '\t\t Add product codes to cart, use "Y" to exit product addition loop',
            '\n c, calc',
            '\t\t Calculate total cost of products in cart',
            '\n h, help',
            '\t\t Print this help text',
        )

    reg = Register(CATALOGUE, DELIVERY, OFFERS)

    if not sys.argv[1]:
        print("Please enter a parameter")
        print(help_txt)

    if sys.argv[1] in ['h', 'help']:
        print(help_txt)

    elif sys.argv[1] in ['c', 'calc']:
        reg.calc_total()
        print('GRAND TOTAL: {}'.format(reg.total))

    elif sys.argv[1] in ['a', 'add']:
        if not sys.argv[2:]:
            print("Please provide a list of correct product code")
        else:
            for p in sys.argv[2:]:
                reg.add_product(p)

