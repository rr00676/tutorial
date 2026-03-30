import pytest

from greet import greet, greet_many


@pytest.mark.parametrize(
    "name, shout, farewell, expected",
    [
        ("World", False, False, "Hello, World!"),
        ("alice", False, False, "Hello, Alice!"),
        ("Alice", True, False, "HELLO, ALICE!"),
        ("Alice", False, True, "Goodbye, Alice!"),
        ("Alice", True, True, "GOODBYE, ALICE!"),
    ],
)
def test_greet(name: str, shout: bool, farewell: bool, expected: str):
    assert greet(name, shout=shout, farewell=farewell) == expected


@pytest.mark.parametrize(
    "names, shout, expected",
    [
        (["Alice", "bob"], False, ["Hello, Alice!", "Hello, Bob!"]),
        (["Alice"], True, ["HELLO, ALICE!"]),
    ],
)
def test_greet_many(names: list, shout: bool, expected: list):
    assert greet_many(names, shout=shout) == expected


@pytest.mark.parametrize("name", ["", "   "])
def test_empty_name_raises(name: str):
    with pytest.raises(ValueError):
        greet(name)


def test_empty_list_raises():
    with pytest.raises(ValueError):
        greet_many([])
