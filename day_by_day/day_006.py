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

    def says(self, words):
        return f'{self._name} says {words}'

    @staticmethod
    def school_headmaster():
        return HogwartsMember('Albus Percival Wulfric Brian Dumbledore', 1881, sex='male')

    # property(fget=None, fset=None, fdel=None, doc=None) -> property attribute
    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear


class Pupil(HogwartsMember):
    """
    Creates a Hogwarts Pupil
    """

    def __init__(self, name: str, birthyear: int, sex: str, house: str, start_year: int, pet: tuple = None):
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

    @property
    def owls(self):
        return self._owls

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


hagrid = HogwartsMember(name='Rubeus Hagrid', birthyear=1928, sex='male')
print(hagrid.age)

harry = Pupil(name='Harry James Potter',
              birthyear=1980,
              sex='male',
              house='Gryffindor',
              start_year=1991,
              pet=('Hedwig', 'owl')
              )

print(harry.owls)
harry.owls = ('Study of Ancient Runes', 'O')
print(harry.owls)
