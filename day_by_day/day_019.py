from dataclasses import dataclass
from typing import NamedTuple


@dataclass(frozen=True)
class DarkArmyMember:
    name: str
    birthyear: int

    @ property
    def leader(self):
        lord_odon = DarkArmyMember('Lord Odon', 1971)
        return lord_odon

    def cast(self, spell):
        print(f"{self.name}: {spell.incantation}!")

keres = DarkArmyMember('Keres Fulford', 1983)
print(keres)
keres.name = 'Adrien'