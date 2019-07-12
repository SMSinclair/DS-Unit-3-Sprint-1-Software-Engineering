from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """Randomly generates a given number of products (default=30), returns them
    as a list."""
    products = []
    for _ in range(num_products):
        name = " ".join(sample(ADJECTIVES, 1) + sample(NOUNS, 1))
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        product = Product(name=name, price=price, weight=weight,
                          flammability=flammability)
        products.append(product)
    return products


def inventory_report(products):
    """Takes a list of products and prints an easy to read summary."""
    unique_names = []
    total_price = 0
    total_weight = 0
    total_flammability = 0
    num_products = len(products)
    
    for item in products:
        if item.name not in unique_names:
            unique_names.append(item.name)
        total_price += item.price
        total_weight += item.weight
        total_flammability += item.flammability

    print("ACME CORPORATION OFFICIAL INVENTORY")
    print(f"Unique product names: {len(unique_names)}")
    print(f"Average price: {total_price/num_products}")
    print(f"Average weight: {total_weight/num_products}")
    print(f"Average flammability: {total_flammability/num_products}")

if __name__ == '__main__':
    inventory_report(generate_products())