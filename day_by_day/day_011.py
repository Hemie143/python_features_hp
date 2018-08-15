from typing import NamedTuple


class DeathEater(NamedTuple):
    name: str
    birthyear: int

    @ property
    def leader(self):
        voldemort = DeathEater('Voldemort', 1926)
        return voldemort

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, birthyear: {self.birthyear})"

lucius = DeathEater('Lucius Malfoy', 1953)
print('Lucius: ', lucius)
print('Leader: ', lucius.leader)

bellatrix = DeathEater('Bellatrix Lestrange', 1951)
print('bellatrix: ', bellatrix)