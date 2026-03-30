import unittest
from greet import greet, greet_many


class TestGreet(unittest.TestCase):
    def test_default(self):
        self.assertEqual(greet("World"), "Hello, World!")

    def test_capitalizes_name(self):
        self.assertEqual(greet("alice"), "Hello, Alice!")

    def test_shout(self):
        self.assertEqual(greet("alice", shout=True), "HELLO, ALICE!")

    def test_shout_default_is_false(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_farewell(self):
        self.assertEqual(greet("Alice", farewell=True), "Goodbye, Alice!")

    def test_farewell_and_shout(self):
        self.assertEqual(greet("Alice", shout=True, farewell=True), "GOODBYE, ALICE!")

    def test_greet_many(self):
        self.assertEqual(greet_many(["Alice", "bob"]), ["Hello, Alice!", "Hello, Bob!"])

    def test_greet_many_shout(self):
        self.assertEqual(greet_many(["Alice"], shout=True), ["HELLO, ALICE!"])


if __name__ == "__main__":
    unittest.main()
