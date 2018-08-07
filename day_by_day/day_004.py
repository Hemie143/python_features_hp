
class HogwartsMember:
    """
    Creates a member of the Hogwarts School of Witchcraft and Wizardy
    """

    # class attribute
    location = 'England'

    def __init__(self, name:str, birthyear:int, sex:str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex

    def __repr__(self):
        return f'{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})'

    # instance method
    def says(self, words):
        return f'{self._name} says {words}'

    @staticmethod
    def school_headmaster():
        return HogwartsMember('Albus Percival Wulfric Brian Dumbledore', 1881)


class Pupil(HogwartsMember):
    """
    Creates a Hogwarts Pupil
    """

    def __init__(self, name:str, birthyear:int, sex:str, house:str, start_year:int, pet: tuple = None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._owls = {
            'Study of Ancient Runes': False,
            'Arithmancy': False,
            'Astronomy': False,
            'Care of Magical Creatures': False,
            'Charms': False,
            'Defence Against the Dark Arts': False,
            'Divination': False,
            'Herbology': False,
            'History of Magic': False,
            'Muggle Studies': False,
            'Potions': False,
            'Transfiguration': False,
        }

    def __repr__(self):
        return(f'{self.__class__.__name__}({self._name}, birthyear: {self.birthyear}, house: {self.house})')

    @staticmethod
    def passed(grade):
        """
        Given a grade, determine if an exam was passed.
        """
        grades = {
            'O': True,
            'Ordinary': True,
            'P': True,
            'Passed': True,
            'A': True,
            'Acceptable': True,
            'P': False,
            'Poor': False,
            'D': False,
            'Dreadful': False,
            'T': False,
            'Troll': False,
        }
        return grades.get(grade, False)

    # Factory function
    @classmethod
    def harry(cls):
        return cls('Harry James Potter', 1980, 'male', 'Gryffindor', start_year=1991, pet=('Hedwig', 'owl'))

class Professor(HogwartsMember):
    """
    Creates a Hogwarts professor
    """

    def __init__(self, name:str, birthyear:int, sex:str, subject:str, house: str = None):
        super().__init__(name, birthyear, sex)
        self.subject = subject
        self.house = house

    def __repr__(self):
        return(f'{self.__class__.__name__}({self._name}, birthyear: {self.birthyear}, subject: {self.subject})')

    @classmethod
    def mcgonagall(cls):
        return cls('Minerva McGonagall', 1935, 'female', 'Transfiguration', house='Gryffindor')


class Ghost(HogwartsMember):
    """
    Creates a Hogwarts ghost
    """

    def __init__(self, name:str, birthyear:int, sex:str, year_of_death:int, house: str = None):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death

        if house is not None:
            self.house = house

    def __repr__(self):
        return(f'{self.__class__.__name__}({self._name}, birthyear: {self.birthyear}, '
               f'year of death: {self.year_of_death})')


if __name__ == "__main__":
    hagrid = HogwartsMember('Rubeus Hagrid', 1928, 'male')
    print(hagrid)
    mcgonagall = Professor.mcgonagall()
    print(mcgonagall)
    harry = Pupil.harry()
    print(harry)
