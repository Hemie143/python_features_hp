

class Potion:
    """ Creates a potion """
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == len(self.ingredients):
            raise StopIteration
        return self.ingredients[self.counter]


flask_of_remembrance = Potion(['raven eggshells', 'tincture of thyme', 'unicorn tears', 'dried onions',
                               'powdered ginger root'])

for ingredient in flask_of_remembrance:
    print(ingredient)
