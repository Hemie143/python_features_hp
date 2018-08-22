import datetime

class HogwartsMember:
    """
    Creates a member of the Hogwarts School of Witchcraft and Wizardy
    """

    # class attribute
    location = 'England'

    def __init__(self, name: str, birthyear: int, sex: str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = {}

    def __repr__(self):
        return f'{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})'

    def says(self, words):
        return f'{self._name} says {words}'

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear

    def add_trait(self, trait, value=True):
        self._traits[trait] = value

    def print_traits(self):
        true_traits = [trait for trait, value in self._traits.items() if value]
        false_traits = [trait for trait, value in self._traits.items() if not value]

        print(f"{self._name} is {', '.join(true_traits)} but not {', '.join(false_traits)}")

    def exhibits_trait(self, trait):
        try:
            value = self._traits[trait]
        except KeyError:
            print(f"{self._name} does not have a character trait with the name '{trait}'")
            return
        if value:
            print(f"Yes, {self._name} is {trait}")
        else:
            print(f"No, {self._name} is not {trait}!")

    @staticmethod
    def school_headmaster():
        return HogwartsMember('Albus Percival Wulfric Brian Dumbledore', 1881, sex='male')


class Pupil(HogwartsMember):
    """
    Creates a Hogwarts Pupil
    """

    def __init__(self, name: str, birthyear: int, sex: str, house: str, start_year: int, pet: tuple = None):
        super(Pupil, self).__init__(name, birthyear, sex)
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

        self._friends = []

    def __repr__(self):
        return f'{self.__class__.__name__}({self._name}, birthyear: {self.birthyear}, house: {self.house})'

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

    def befriend(self, person):
        """ Adds another person to your list of friends """
        if person.__class__.__name__ != 'CastleKilmereMember' and self.house != 'Slytherin' and person.house == 'Slytherin':
            print("Are you sure you want to be friends with someone from Slytherin?")
        self._friends.append(person)
        print(f"{person.name} is now your friend!")

    @property
    def current_year(self):
        now = datetime.datetime.now().year
        return (now - self.start_year) + 1

    @property
    def owls(self):
        return self._owls

    @property
    def friends(self):
        return f"{self._name}'s current friends are {[person.name for person in self._friends]}"

    @owls.setter
    def owls(self, subject_and_grade):

        try:
            subject, grade = subject_and_grade
        except ValueError:
            raise ValueError('Pass an iterable with two items: subject and grade')
        passed = self.passed(grade)
        if passed:
            self._owls[subject] = True
        else:
            print('The exam was not passed so now OWL was awarded!')

    @owls.deleter
    def owls(self):
        print("Caution, you are deleting this student's OWL's! "
              "You should only do that if she/he dropped out of school without passing any exam!")
        del self._owls

    # Factory function
    @classmethod
    def harry(cls):
        return cls('Harry James Potter', 1980, 'male', 'Gryffindor', start_year=1991, pet=('Hedwig', 'owl'))

    @classmethod
    def ron(cls):
        return cls('Ronald Bilius Weasley', 1980, 'male', 'Gryffindor', start_year=1991, pet=('Pigwidgeon', 'owl'))

    @classmethod
    def hermione(cls):
        return cls('Hermione Granger', 1979, 'female', 'Gryffindor', start_year=1991, pet=('Crookkshanks', 'cat'))

    @classmethod
    def malfoy(cls):
        return cls('Draco Lucius Malfoy', 1980, 'male', 'Slytherin', start_year=1991, pet=('Unnamed', 'owl'))


hagrid = HogwartsMember(name='Rubeus Hagrid', birthyear=1928, sex='male')
hagrid.add_trait("kind")
hagrid.add_trait("monster-loving")
hagrid.add_trait("impatient", value=False)

hagrid.print_traits()
hagrid.exhibits_trait("kind")
hagrid.exhibits_trait("impatient")
hagrid.exhibits_trait("bearded")
