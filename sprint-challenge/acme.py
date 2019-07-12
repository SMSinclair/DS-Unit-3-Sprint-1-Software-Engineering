import random


class Product:
    """ A class to organize the goods managed and sold by the Acme Corporation.
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """Calculates price divided by weight and returns an
        appropriate message"""

        ratio = self.price/self.weight
        if ratio < 0.5:
            return("Not so stealable...")
        elif ratio < 1.0:
            return("Kinda stealable.")
        else:
            return("Very stealable!")

    def explode(self):
        """Calculates flammability times weight and returns an appropriate
        message"""
        product = self.flammability * self.weight
        if product < 10:
            return("...fizzle.")
        elif product < 50:
            return("...boom!")
        else:
            return("...BABOOM!")


class BoxingGlove(Product):
    """A subclass of Product that represents a boxing glove."""
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        """Override of parent explode method"""
        print("...it's a glove.")

    def punch(self):
        """Float like a butterfly sting like a bee."""
        if self.weight < 5:
            print("That tickles.")
        elif self.weight < 15:
            print("Hey, that hurt!")
        else:
            print("OUCH!")