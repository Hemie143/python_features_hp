import datetime

from dataclasses import dataclass
from typing import NamedTuple


class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
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

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear

    @staticmethod
    def school_headmaster():
        return CastleKilmereMember('Redmond Dalodore', 1939, sex='male')

    def says(self, words):
        return f'{self._name} says {words}'

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



class Pupil(CastleKilmereMember):
    """
    Creates a Castle Kilmere Pupil
    """

    def __init__(self, name: str, birthyear: int, sex: str, house: str, start_year: int, pet: tuple = None):
        # super(Pupil, self).__init__(name, birthyear, sex)
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year
        self.known_spells = set()

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._elms = {
            'Broomstick Flying': False,
            'Art': False,
            'Magical Theory': False,
            'Foreign Magical Systems': False,
            'Charms': False,
            'Defence Against Dark Magic': False,
            'Divination': False,
            'Herbology': False,
            'History of Magic': False,
            'Potions': False,
            'Transfiguration': False
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
            'Horrible': False,
            'T': False,
            'Troll': False,
        }
        return grades.get(grade, False)

    def befriend(self, person):
        """ Adds another person to your list of friends """
        if person.__class__.__name__ != 'CastleKilmereMember' \
                and self.house != 'House of Ambition' \
                and person.house == 'House of Ambition':
            print("Are you sure you want to be friends with someone from House of Ambition?")
        self._friends.append(person)
        print(f"{person.name} is now your friend!")

    def learn_spell(self, spell):
        """
        Allows a pupil to learn a spell, given that he/she is old enough
        """
        if spell.min_year is not None:
            if self.current_year >= spell.min_year:
                print(f"{self._name} now knows spell {spell.name}")
                self.known_spells.add(spell)
            elif self.exhibits_traits('highly intelligent'):
                print(f"{self._name} now knows spell {spell.name}")
                self.known_spells.add(spell)
            if self.current_year < spell.min_year:
                print(f"{self._name} is too young to study this spell!")
        elif spell.__class__.__name__ in ['Hex', 'Curse']:
            # Only House of Ambition would study hexes and curses
            if self.house == 'House of Ambition':
                print(f"{self._name} now knows spell {spell.name}")
                self.known_spells.add(spell)
            else:
                print(f"How dare you study a hex or curse?!")

    def cast_spell(self, spell):
        """
        Allows a pupil to cast a spell
        """
        if spell.__class__.__name__ == 'Curse':
            print(f"This is dark magic - stay away from performing curses!")
        elif spell.__class__.__name__ == 'Hex':
            if self.house == 'House of Ambition':
                print(f"{self._name}: {spell.incantation}!")
            else:
                print(f"You shouldn't cast a hex, that's mean!")
        elif spell in self.known_spells:
            print(f"{self._name}: {spell.incantation}!")
        elif spell.name not in self.known_spells:
            print(f"You can't cast the {spell.name} spell correctly - you have to study it first! ")

    @property
    def current_year(self):
        now = datetime.datetime.now().year
        return (now - self.start_year) + 1

    @property
    def elms(self):
        return self._elms

    @property
    def friends(self):
        return f"{self._name}'s current friends are {[person.name for person in self._friends]}"

    @elms.setter
    def elms(self, subject_and_grade):

        try:
            subject, grade = subject_and_grade
        except ValueError:
            raise ValueError('Pass an iterable with two items: subject and grade')
        passed = self.passed(grade)
        if passed:
            self._elms[subject] = True
        else:
            print('The exam was not passed so now ELM was awarded!')

    @elms.deleter
    def elms(self):
        print("Caution, you are deleting this student's ELM's! "
              "You should only do that if she/he dropped out of school without passing any exam!")
        del self._elms

    # Factory function
    @classmethod
    def cleon(cls):
        return cls('Cleon Bery', 2008, 'male', 'House of Courage', 2018, ('Cotton', 'owl'))

    @classmethod
    def flynn(cls):
        return cls('Flynn Gibbs', 2008, 'male', 'House of Courage', 2018, ('Twiggles', 'owl'))

    @classmethod
    def cassidy(cls):
        return cls('Cassidy Ambergem', 2007, 'female', 'House of Courage', 2018, ('Ramses', 'cat'))

    @classmethod
    def adrien(cls):
        return cls('Adrien Fulford', 2008, 'male', 'House of Ambition', 2018, ('Unnamed', 'owl') )

    @classmethod
    def aurora(cls):
        return cls('Aurora Gibbs', 1981, 'female', 'House of Courage', 1992)


class Professor(CastleKilmereMember):
    """
    Creates a Castle Kilmere professor
    """

    def __init__(self, name: str, birthyear: int, sex: str, subject: str, house: str = None):
        # super(Professor, self).__init__(name, birthyear, sex)
        super().__init__(name, birthyear, sex)
        self.subject = subject
        self.house = house

    def __repr__(self):
        return f'{self.__class__.__name__}({self._name}, birthyear: {self.birthyear}, subject: {self.subject})'

    @classmethod
    def mirren(cls):
        return cls('Miranda Mirren', 1963, 'female', 'Transfiguration', 'House of Courage')

    @classmethod
    def blade(cls):
        return cls('Blade Bardock', 1988, 'male', 'Potions', 'House of Ambition')

    @classmethod
    def briddle(cls):
        return cls('Birdie Briddle', 1931, 'female', 'Herbology', 'House of Loyalty')

    @classmethod
    def radford(cls):
        return cls('Rupert Radford', 1958, 'male', 'Charms', 'House of Creativity')

    @classmethod
    def giddings(cls):
        return cls('Gabriel Giddings', 1974, 'male', 'Broomstick Flying', 'House of Wisdom')


class Ghost(CastleKilmereMember):
    """
    Creates a Castle Kilmere ghost
    """

    def __init__(self, name: str, birthyear: int, sex: str, year_of_death: int, house: str = None):
        # super(Ghost, self).__init__(name, birthyear, sex)
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death
        self.house = house

    def __repr__(self):
        return f'{self.__class__.__name__}({self._name}, birthyear: {self.birthyear}, ' \
               f'year of death: {self.year_of_death})'

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear

    @classmethod
    def mocking_knight(cls):
        return cls('The Mocking Knight', 1401, 'male', 1492, 'House of Courage')

    @classmethod
    def gray_groom(cls):
        return cls('The Gray Groom', 1000, 'male', 1050, 'House of Loyalty')

    @classmethod
    def scary_scoundrel(cls):
        return cls('Scary Scoundrel', 983, 'male', 1010, 'House of Ambition')

    @classmethod
    def old_lady(cls):
        return cls('The Old Lady', 983, 'male', 996, 'House of Wisdom')

    @classmethod
    def boneless_barde(cls):
        return cls("The Boneless Bard", 1211, 'male', 1288, 'House of Creativity')


class DarkArmyMember(NamedTuple):
    name: str
    birthyear: int

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, birthyear: {self.birthyear})"

    @ property
    def leader(self):
        lord_odon = DarkArmyMember('Lord Odon', 1971)
        return lord_odon

    def cast(self, spell):
        print(f"{self.name}: {spell.incantation}!")


class Charm:
    """ Creates a charm """
    def __init__(self, incantation: str, difficulty: str= None, effect: str = None):
        self.incantation = incantation
        self.difficulty = difficulty
        self.effect = effect

    def __repr__(self):
        return f'{self.__class__.__name__}({self.incantation}, {self.difficulty}, {self.effect})'

    def cast(self):
        print(f"{self.incantation}!")

    @classmethod
    def lumos(cls):
        return cls('Lumos', 'simple', 'Illuminates the wand tip')

    @classmethod
    def wingardium_leviosa(cls):
        return cls('Wingardium Leviosa', 'simple', 'Makes objects fly')

@dataclass(order=True)
class House:
    name: str
    traits: list
    head: Professor
    ghost: Ghost
    founded_in: int = 991

    def current_age(self):
        now = datetime.datetime.now().year
        return (now - self.founded_in) + 1


if __name__ == "__main__":
    mocking_knight = Ghost.mocking_knight()
    gray_groom = Ghost.gray_groom()
    scary_scoundrel = Ghost.scary_scoundrel()
    old_lady = Ghost.old_lady()

    mirren = Professor.mirren()
    briddle = Professor.briddle()
    blade = Professor.blade()
    radford = Professor.radford()
    print('Age of Professor Radford: ', radford.age)

    house_of_courage = House('House of Courage',
                       ['bravery', 'nerve', 'courage'],
                       mirren,
                       mocking_knight)
    print('house_of_courage: ', house_of_courage)

    house_of_loyalty = House('House of Loyalty',
                       ['loyalty', 'fairness', 'patience', 'kindness'],
                       briddle,
                       gray_groom)
    print('house_of_loyalty: ', house_of_loyalty)

    house_of_ambition = House('House of Ambition',
                      ['cunning', 'ambition', 'determination'],
                      blade,
                      scary_scoundrel)
    print('house_of_ambition: ', house_of_ambition)

    house_of_wisdom = House('House of Wisdom',
                      ['intelligence', 'wit', 'wisdom'],
                      radford,
                      old_lady)
    print('house_of_wisdom: ', house_of_wisdom)
