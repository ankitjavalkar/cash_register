# Cash Register App

### Quick Help

```
Usage: python3 cash_register.py [OPTIONS]...

a, add [PRODUCT-CODE1] [PRODUCT-CODE2] [PRODUCT-CODE3]...	 Add product codes to cart, and calculate total

h, help	 Print this help text
```

### Example

```

	$> python3 cash_register.py add B01 B01 R01 R01 R01
	$> GRAND TOTAL: $98.27
```

### How To Setup

1. Create/Edit the config.py file to define your own catalogue, Delivery pricing and Offer structure (See config.py for documentation on how to structure the data)

Note: The config.py has already been configured based on the given example

1. Run the command ```python3 cash_register.py add <Prod_Code_1> <Prod_Code_2> <Prod_Code_3>```
1. The grand total for the list of products is output to the console

#### Assumptions:
1. The offers list is sorted by the lowest total amount for any given offer
1. The offer list needs to be constructed such that the total amount / math expression for any particular pattern needs to be specified

#### Possible Ways To Improve:
1. The logic to calculate the offers and the way it's calculated can be definitely improved to support more complex patterns.
1. Can ingest files instead of creating pythonic data structures directly.
1. Can add Unit Tests.


