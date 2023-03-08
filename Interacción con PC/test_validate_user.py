
import unittest
from unittest import TestCase

from validations import validate_user

class TestValidateUser(unittest, TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validuser", 3), True)

    def test_too_sort(self):
        self.assertEqual(validate_user("inv", 5), False)

    def test_too_characters(self):
        self.assertEqual(validate_user("invalid user", 1), False)

    def test_invalid_min_len(self):
        self.assertRaises(ValueError, validate_user, "user", -1)

unittest.main()


