import pytest
from python_features_hp.magic_universe import CastleKilmereMember
from python_features_hp.error import TraitDoesNotExistError

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
    assert bromley.name == 'Bromley Huckabee'
    assert bromley.birthyear == 1959
    assert bromley.sex == 'male'


def test_add_positive_traits(bromley):
    bromley.add_trait('kind')
    bromley.add_trait('wild')
    assert bromley._traits == {'kind': True, 'wild': True}


def test_add_negative_trait(bromley):
    bromley.add_trait('mean', False)
    assert bromley._traits == {'mean': False}


def test_exhibit_traits(bromley_with_traits):
    assert bromley_with_traits.exhibits_trait('kind') is True
    assert bromley_with_traits.exhibits_trait('mean') is False
    with pytest.raises(TraitDoesNotExistError):
        bromley_with_traits.exhibits_trait('smart')


def test_print_traits(capfd, bromley_with_traits):
    bromley_with_traits.print_traits()
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'Bromley Huckabee is kind, tidy-minded but not mean'


def test_init_raises_exception_with_missing_arguments():
    with pytest.raises(TypeError):
        bromley = CastleKilmereMember()


def test_says(bromley):
    assert bromley.says("Hi Cleon!") == "Bromley Huckabee whispers: Hi Cleon."


def test_name_property(bromley):
    assert bromley.name == 'Bromley Huckabee'


def test_age_property(bromley):
    assert bromley.age == 59        # Only in 2018


def test_repr_output(capfd, bromley):
    print(bromley)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'CastleKilmereMember(Bromley Huckabee, birthyear: 1959)'