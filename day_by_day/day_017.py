# Data classes
# PEP: https://www.python.org/dev/peps/pep-0557/

from dataclasses import dataclass
import datetime

@dataclass
class House:
    name: str
    traits: list
    founded_in: int = 991

    '''
    Automatically added:
    def __init__(self, name: str, traits: list):
        self.name = name
        self.traits = traits
        
    def __repr__
    def __eq__
    '''

    def current_age(self):
        now = datetime.datetime.now().year
        return (now - self.founded_in) +1


house_of_courage = House('House of Courage', ['bravery', 'nerve', 'courage'])
house_of_loyalty = House('House of Loyalty', ['loyalty', 'fairness', 'patience', 'kindness'])

print(house_of_courage == house_of_loyalty)
print(house_of_courage == house_of_courage)