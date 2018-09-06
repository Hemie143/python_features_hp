import datetime
from typing import NamedTuple
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


class Spell(metaclass=ABCMeta):
    """ Creates a spell """
    def __init__(self, name: str, incantation: str, effect: str, difficulty: str, min_year: int = None):
        self.name = name
        self.incantation = incantation
        self.effect = effect
        self.difficulty = difficulty
        self.min_year = min_year

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
    """ Creates a Charm - a spell that alters the inherent qualities of an object"""

    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = None, min_year: int = None):
        super().__init__(name, incantation, effect, difficulty, min_year)

    @property
    def defining_feature(self):
        return("Alteration of the object's inherent qualities, that is, its behaviour and capabilities")

    def cast(self):
        print(f"{self.incantation}!")

    @classmethod
    def stuporus_ratiato(cls):
        return cls('Stuporus Ratiato', 'Stuporus Ratiato', 'Makes objects fly', 'simple', 1)

    @classmethod
    def liberula(cls):
        return cls('Liberula', 'Liberula', 'Allows a person to breathe under water', 'difficult', 5)


class Transfiguration(Spell):
    """ Creates a transfiguration - a spell that alters the form or appearance of an object """

    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = None, min_year: int = None):
        super().__init__(name, incantation, effect, difficulty, min_year)

    @property
    def defining_feature(self):
        return("Alteration of the object's form or appearance")

    def cast(self):
        print(f"{self.incantation}!")

    @classmethod
    def alterator_canieo(cls):
        return cls('Alteraro Canieo', 'Alteraro Canieo', 'Turns an object into a can', 'simple', 2)


class Jinx(Spell):
    """ Creates a jinx - a spell whose effects are irritating but amusing """

    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = None, min_year: int = None):
        super().__init__(name, incantation, effect, difficulty, min_year)

    @property
    def defining_feature(self):
        return("Minor dark magic - a spell whose effects are irritating but amusing, almost playful and minor "
               "inconvenience to the target")

    def cast(self):
        print(f"{self.incantation}!")

    @classmethod
    def inceptotis(cls):
        return cls('Inceptotis', 'Inceptotis', 'Make a person talk baby talk', 'simple')


class Hex(Spell):
    """ Creates a hex - a spell that affects an object in a negative manner """

    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = None, min_year: int = None):
        super().__init__(name, incantation, effect, difficulty, min_year)

    @property
    def defining_feature(self):
        return("Medium dark magic - Affects an object in a negative manner. Major inconvenience to the target.")

    def cast(self):
        print(f"{self.incantation}!")

    @classmethod
    def rectaro(cls):
        return cls('Rectaro', 'Rectaro', 'Exchange a persons arms and legs', 'difficult')


class Curse(Spell):
    """ Creates a hex - a spell that affects an object in a strongly negative manner """

    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = None, min_year: int = None):
        super().__init__(name, incantation, effect, difficulty, min_year)

    @property
    def defining_feature(self):
        return("Worst kind of dark magic - Intended to affect an object in a strongly negative manner.")

    def cast(self):
        print(f"{self.incantation}!")

    @classmethod
    def fiera_satanotis(cls):
        return cls('Torture spell', 'Fiera Satanotis', 'Tortures a person, makes person suffer deeply', 'difficult')


class CounterSpell(Spell):
    """ Creates a counter-spell - a spell that inhibits the effect of another spell """

    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = None, min_year: int = None):
        super().__init__(name, incantation, effect, difficulty, min_year)

    @property
    def defining_feature(self):
        return("Inhibits the effects of another spell")

    def cast(self):
        print(f"{self.incantation}!")

    @classmethod
    def mufindo_immolim(cls):
        return cls('Mufindo Immolim', 'Mufindo Immolim',
                   'Counteracts the immobilisation spell that prevents a person from moving', 'simple')


class HealingSpell(Spell):
    """ Creates a healing spell - a spell that improves the condition of a living object """

    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = None, min_year: int = None):
        super().__init__(name, incantation, effect, difficulty, min_year)

    @property
    def defining_feature(self):
        return("Improves the condition of a living object")

    def cast(self):
        print(f"{self.incantation}!")

    @classmethod
    def porim_perfite(cls):
        return cls('Wound healing spell', 'Porim Perfite',
                   'Heals all kinds of wounds, even bad ones', 'difficult')

if __name__ == '__main__':
    charm = Charm.liberula()
    print('charm: ', charm)

    transfiguration = Transfiguration.alterator_canieo()
    print(transfiguration.cast())

    jinx = Jinx.inceptotis()
    print('jinx: ', jinx)

    hex_ = Hex.rectaro()
    print(hex_.cast())

    curse = Curse.fiera_satanotis()
    print('curse: ', curse)

    healing_spell = HealingSpell.porim_perfite()
    print(healing_spell.cast())

    counter_spell = CounterSpell.mufindo_immolim()
    print(counter_spell.cast())
