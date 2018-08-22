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

spell = Spell('Stuporus Ratiato', 'Stuporus Ratiato', 'Makes objects fly')