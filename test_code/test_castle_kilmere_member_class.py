import pytest

from python_features_hp.magic_universe import CastleKilmereMember

def say_words(person, words):
    return f"{person} says: {words}"

def test_say_words():
    assert say_words('Aurora', 'Careful Quintus!') == 'Aurora says: Careful Quintus!'

def test_correctness_of_attributes_():
    bromley = CastleKilmereMember('Bromley Huckabee', 1959, 'male')
    assert bromley.name == 'Bromley Huckabee'
    assert bromley.birthyear == 1959
    assert bromley.sex == 'male'

def test_add_positive_traits():
    bromley = CastleKilmereMember('Bromley Huckabee', 1959, 'male')
    bromley.add_trait('kind')
    bromley.add_trait('tidy-minded')
    assert bromley._traits == {'kind': True, 'tidy-minded': True}

def test_add_negative_traits():
    bromley = CastleKilmereMember('Bromley Huckabee', 1959, 'male')
    bromley.add_trait('mean', False)
    assert bromley._traits == {'mean': False}

def test_exhibit_traits():
    bromley = CastleKilmereMember('Bromley Huckabee', 1959, 'male')
    bromley.add_trait('kind')
    bromley.add_trait('tidy-minded')
    bromley.add_trait('mean', False)
    assert bromley.exhibits_trait('kind') is True
    assert bromley.exhibits_trait('mean') is False
    assert bromley.exhibits_trait('smart') is None
