# Data classes
# PEP: https://www.python.org/dev/peps/pep-0557/

from dataclasses import dataclass


@dataclass
class House:
    name: str
    traits: list


house_of_courage = House('House of Courage', ['bravery', 'nerve', 'courage'])