from abc import ABCMeta, abstractmethod


class Spell(metaclass=ABCMeta):
    """ Creates a charm """
    def __init__(self, name: str, incantation: str, effect: str):
        self.name = name
        self.incantation = incantation
        self.effect = effect

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.name}, "
               f"incantation: '{self.incantation}', effect: {self.effect})")

    @abstractmethod
    def cast(self):
        pass

    @property
    @abstractmethod
    def defining_feature(self):
        pass

class Charm(Spell):

    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = None, min_year: int = None):
        super(Charm, self).__init__(name, incantation, effect)
        self.difficulty = difficulty
        self.min_year = min_year

    @property
    def defining_feature(self):
        return("Alteration of the object's inherent qualities, that is, its behaviour and capabilities")

    def cast(self):
        print(f"{self.incantation}!")

charm = Charm('Stuporus Ratiato', 'Stuporus Ratiato', 'Makes objects fly', 'simple')
print(charm)