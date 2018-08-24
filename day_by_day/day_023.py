# https://docs.python.org/3/library/stdtypes.html#typecontextmanager
# Context managers must implement __enter__ and __exit__

class Letter:
    def __init__(self, letter_name):
        self.letter_name = letter_name

    def __enter__(self):
        self.letter = open(self.letter_name, 'w')
        return self.letter

    def __exit__(self, exc_type, exc_value, traceback):
        if self.letter:
            self.letter.close()

with Letter('dear_bromley.txt') as letter:
    letter.write("Hi Bromley! \n"
                 "Can Flynn, Cassidy and I stop by for a tea this afternoon? \n"
                 "Cleon")

# Process: https://docs.python.org/3/reference/compound_stmts.html#with
# 1. "with" invokes a context manager
# 2. __exit__ is loaded
# 3. __enter__ is onvoked
# 4. value return by __enter__ is bound to identifier after "as"
# 5. code in body of with is executed
# 6. __exit__ is inovked no matter what
