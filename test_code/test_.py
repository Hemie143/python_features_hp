def say_words(person, words):
    return f"{person} says: '{words}'"

def test_say_words():
    assert say_words("Aurora", "Careful Quintus!") == "Aurora says: 'Careful Quintus!'"