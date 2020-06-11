from pythonic_garage_band.pythonic_garage_band import (
    Band,
    Musician,
    Guitarist,
    Bassist,
    Drummer,
)

# Roger's demo Front Row

# https://realpython.com/instance-class-and-static-methods-demystified/

# Socratica Classes video

def test_Band_class_exists():
    assert Band


# A Band instance should have a name attribute which is a string.
def test_Band_name_returns():
    expected = "Flying Penguins, members: ['Fred', 'Roy', 'Beevis']"
    actual = Band("Flying Penguins", ['Fred', 'Roy', 'Beevis'])
    assert actual == expected

# A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.

# A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.

# A Band instance should have appropriate __str__ and __repr__ methods.

# A Band should have a class method to_list which returns a list of previously created Band instances

def test_Musician_class_exists():
    assert Musician


def test_Guitarist_class_exists():
    assert Guitarist


def test_Bassist_class_exists():
    assert Bassist


def test_Drummer_class_exists():
    assert Drummer

