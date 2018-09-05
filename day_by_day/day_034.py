from collections import Counter
from python_features_hp.magic_universe import Potion

flask_of_remembrance = Potion(['raven eggshells', 'tincture of thyme', 'unicorn tears',
                               'dried onions', 'powdered ginger root'])

vial_of_anger = Potion(['dried dragon skin', 'leeches', 'shredded elephant tusk',
                        'horned flies', 'earthworm juice', 'dried onions'])

ancient_wisdom = Potion(['tincture of thyme', 'leeches', 'drakus of flower', 'lavender sprig',
                         'earthworm juice', 'cactus juice', 'dried onions'])

brew_of_lies = Potion(['horned flies', 'leeches', 'drakus of flower', 'horned flies',
                       'unicorn tears', 'cactus juice'])

all_potions = [flask_of_remembrance, vial_of_anger, ancient_wisdom, brew_of_lies]

shopping_list = Counter()

for potion in all_potions:
    for ingredient in potion:
        shopping_list[ingredient] += 1

print(f"Final shopping list: {shopping_list}")

# https://docs.python.org/3/library/collections.html#collections.Counter