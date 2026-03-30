import unittest
from main import greet


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


if __name__ == "__main__":
    unittest.main()
