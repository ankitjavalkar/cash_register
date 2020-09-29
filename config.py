"""
Catalogue specifications table

Each key value pair represents a single entry in the catalogue

Each catalogue entry has Product Code as Key and a list as value
The list contains 2 elements - Product name and Product price
"""
CATALOGUE = {
    'R01': ['Red Widget', 32.95],
    'G01': ['Green Widget', 24.95],
    'B01': ['Blue Widget', 7.95],
}


"""
Delivery Charges table

Setup as a list of lists where each inner list denotes a deliver charge spec

Each delivery charge spec is written in the format:
['lower_bound_total_price', 'upper_bound_total_price', 'delivery_charges']
"""
DELIVERY = [
    [0.0, 50.0, 4.95],
    [50.0,  90.0, 2.95],
    [90.0, 9999999.0, 0.0],
]


"""
Offer specifications table

The Offers specification is a list of dictionaries where each dictionary
represents one offer

Each offer contains two keys:

pattern : A list representing the pattern on which a particular offer can be applied
amt : The resultant price of that offer, this can be a float or an expression
"""
OFFERS = [
    {'pattern': ['R01', 'R01'], 'amt': 49.42},
    # Can also use:
    # {'pattern': ['R01', 'R01'], 'amt': CATALOGUE['R01'][1] * 1.5},
]
