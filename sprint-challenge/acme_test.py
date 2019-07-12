#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_weight(self):
        """Tests default weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability_explode(self):
        """Builds an object with different values and and ensures their
        stealability() and explode() methods work as they should."""
        # Create instances to test
        not_stealable = Product(name="test1", price=1, weight=5)
        kinda_stealable = Product(name="test2", price=7, weight=10)
        very_stealable = Product(name="test3", price=20, weight=10)
        fizzle = Product(name="test4", flammability=1, weight=5)
        boom = Product(name="test5", flammability=2, weight=8)
        baboom = Product(name="test6", flammability=10, weight=10)
        # Test the instances
        self.assertEqual(not_stealable.stealability(), "Not so stealable...")
        self.assertEqual(kinda_stealable.stealability(), "Kinda stealable.")
        self.assertEqual(very_stealable.stealability(), "Very stealable!")
        self.assertEqual(fizzle.explode(), "...fizzle.")
        self.assertEqual(boom.explode(), "...boom!")
        self.assertEqual(baboom.explode(), "...BABOOM!")


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme product reports are in ship shape!"""
    def test_default_num_products(self):
        """Checks that it really does receive a list of length 30"""
        product_list = generate_products()
        self.assertEqual(len(product_list), 30)
    def test_legal_names(self):
        """Checks that the generated names for a default batch of products are
        all valid possible names to generate."""
        product_list = generate_products()
        for prod in product_list:
            noun = prod.name.split(" ")[1]
            adjective = prod.name.split(" ")[0]
            self.assertIn(noun, NOUNS)
            self.assertIn(adjective, ADJECTIVES)

if __name__ == '__main__':
    unittest.main()
