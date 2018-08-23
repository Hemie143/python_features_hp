
# https://github.com/zotroneneis/magical_universe/commit/758b61c3a4bd8fa335adb208e24141e670d19d61

class Pupil(CastleKilmereMember):

    def __init__(self, name: str, birthyear: int, sex: str, house: str, start_year: int, pet: tuple = None):
        super(Pupil, self).__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year
        self.known_spells = set()

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
