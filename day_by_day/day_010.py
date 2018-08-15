from collections import namedtuple
from typing import NamedTuple

# pet = ('pet_name', 'pet_type')

Pet = namedtuple('Pet', 'pet_name pet_type')
harrys_pet = Pet('Hedwig', 'owl')
print(harrys_pet.pet_name)

class Pet(NamedTuple):
    pet_name: str
    pet_type: str

    def __repr__(self):
        return f"{self.pet_name}, {self.pet_type}"

harrys_pet = Pet('Hedwig', 'owl')
print('harrys_pet: ', harrys_pet)
