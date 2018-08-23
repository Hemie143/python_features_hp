# Data classes
# PEP: https://www.python.org/dev/peps/pep-0557/

from dataclasses import dataclass
import datetime


@dataclass(order=True)
class House:
    name: str
    traits: list
    founded_in: int = 991

    def current_age(self):
        now = datetime.datetime.now().year
        return (now - self.founded_in) + 1


house_of_courage = House('House of Courage', ['bravery', 'nerve', 'courage'])
house_of_loyalty = House('House of Loyalty', ['loyalty', 'fairness', 'patience', 'kindness'])

print(house_of_loyalty < house_of_courage)
