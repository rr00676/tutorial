import pytest

from greet import greet, greet_many


def test_default():
    assert greet("World") == "Hello, World!"


def test_capitalizes_name():
    assert greet("alice") == "Hello, Alice!"


def test_shout():
    assert greet("alice", shout=True) == "HELLO, ALICE!"


def test_shout_default_is_false():
    assert greet("Alice") == "Hello, Alice!"


def test_farewell():
    assert greet("Alice", farewell=True) == "Goodbye, Alice!"


def test_farewell_and_shout():
    assert greet("Alice", shout=True, farewell=True) == "GOODBYE, ALICE!"


def test_greet_many():
    assert greet_many(["Alice", "bob"]) == ["Hello, Alice!", "Hello, Bob!"]


def test_greet_many_shout():
    assert greet_many(["Alice"], shout=True) == ["HELLO, ALICE!"]


def test_empty_name_raises():
    with pytest.raises(ValueError):
        greet("")


def test_blank_name_raises():
    with pytest.raises(ValueError):
        greet("   ")


def test_empty_list_raises():
    with pytest.raises(ValueError):
        greet_many([])
