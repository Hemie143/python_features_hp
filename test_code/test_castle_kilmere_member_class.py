import pytest
from python_features_hp.magic_universe import CastleKilmereMember


@pytest.fixture()
def bromley():
    bromley = CastleKilmereMember('Bromley Huckabee', 1959, 'male')
    return bromley


@pytest.fixture()
def bromley_with_traits():
    bromley = CastleKilmereMember('Bromley Huckabee', 1959, 'male')
    bromley.add_trait('kind')
    bromley.add_trait('tidy-minded')
    bromley.add_trait('mean', False)
    return bromley


def test_correctness_of_attributes_(bromley):
    assert bromley._name == 'Bromley Huckabee'
    assert bromley.birthyear == 1959
    assert bromley.sex == 'male'


def test_add_positive_traits(bromley):
    bromley.add_trait('kind')
    bromley.add_trait('tidy-minded')
    assert bromley._traits == {'kind': True, 'tidy-minded': True}


def test_add_negative_trait(bromley):
    bromley.add_trait('mean', False)
    assert bromley._traits == {'mean': False}


def test_exhibit_traits(bromley_with_traits):
    assert bromley_with_traits.exhibits_trait('kind') is True
    assert bromley_with_traits.exhibits_trait('mean') is False
    assert bromley_with_traits.exhibits_trait('smart') is None
