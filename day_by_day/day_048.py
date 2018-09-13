from collections import defaultdict

class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    # class attribute
    location = 'England'

    def __init__(self, name: str, birthyear: int, sex: str):
        self._name = name
        if type(birthyear) is not int:
            raise error.InvalidBirthyearError("The birthyear is not a valid integer. Try something like 1991")
        self.birthyear = birthyear
        self.sex = sex
        self._traits = defaultdict(lambda: False)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})'

    @property
    def name(self):
        return self._name

    def add_trait(self, trait, value=True):
        self._traits[trait] = value

    def print_traits(self):
        true_traits = [trait for trait, value in self._traits.items() if value]
        false_traits = [trait for trait, value in self._traits.items() if not value]

        print(f"{self._name} is {', '.join(true_traits)} but not {', '.join(false_traits)}")

    def exhibits_trait(self, trait):
        value = self._traits[trait]
        if value:
            print(f"Yes, {self._name} is {trait}!")
        else:
            print(f"No, {self._name} is not {trait}!")
        return value


if __name__ == "__main__":
    bromley = CastleKilmereMember('Bromley Huckabee', 1959, 'male')

    bromley.add_trait('tidy-minded')
    bromley.add_trait('kind')

    bromley.exhibits_trait('kind')
    bromley.exhibits_trait('mean')
