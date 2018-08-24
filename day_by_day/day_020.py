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

    def whisper(function):
        def wrapper(*args):
            original_output = function(*args)
            # We split the output in two parts, to replace "says" by "whispers"
            first_part, words = original_output.split(' says: ')
            # We need to remove exclamation marks when whispering
            words = words.replace('!', '.')
            new_output = f"{first_part} whispers: {words}"
            return new_output
        return wrapper

    @whisper
    def says(self, words):
        return f'{self._name} says: {words}'


class Pupil(CastleKilmereMember):
    """
    Creates a Castle Kilmere Pupil
    """

    def __init__(self, name: str, birthyear: int, sex: str, house: str, start_year: int, pet: tuple = None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year
        self.known_spells = set()

        if pet is not None:
            self.pet_name, self.pet_type = pet

    @classmethod
    def aurora(cls):
        return cls('Aurora Gibbs', 1981, 'female', 'House of Courage', 1992)



aurora = Pupil.aurora()
print(aurora.says("Be careful Quintus!"))
