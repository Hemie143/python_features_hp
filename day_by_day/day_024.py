

class Letter:
    total_number_of_letters = 0

    def __init__(self, letter_name):
        self.letter_name = letter_name
        self.__class__.total_number_of_letters += 1

    def __enter__(self):
        self.letter = open(self.letter_name, 'w')
        return self.letter

    def __exit__(self, exc_type, exc_value, traceback):
        if self.letter:
            self.letter.close()


class CastleKilmereMember:



    def write_letter(self, recipient, content):
        letter_name = f"dear_{recipient}.txt"
        with Letter(letter_name) as l:
            l.write(content)

if __name__ == "__main__":
    cleon = Pupil.cleon()
    letter_content = "Hi Bromley! \nCan Flynn, Cassidy and I stop by for a tea this afternoon? \nCleon"
    cleon.write_letter('Bromley', letter_content)

    print(f"Total number of letter created so far: {Letter.total_number_of_letters}")