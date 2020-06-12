import pytest

from pythonic_garage_band.pythonic_garage_band import (
    Band,
    Musician,
    Guitarist,
    Bassist,
    Drummer,
)


def test_Band_class_exists():
    assert Band


def test_Musician_class_exists():
    assert Musician


def test_Guitarist_class_exists():
    assert Guitarist


def test_Bassist_class_exists():
    assert Bassist


def test_Drummer_class_exists():
    assert Drummer


def test_Band_one_name_returns():
    expected_name = "Flying Penguins"
    actual = Band("Flying Penguins", [])
    assert actual.name == expected_name


def test_guitarist_returns():
    actual = Guitarist('Toby')
    expected = "Toby"
    assert actual.name == expected


