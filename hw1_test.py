from importlib.metadata import Lookup

import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count1(self):
        input = "meow"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)

    def test_vowel_count2(self):
        input = "omnitrix"
        result = hw1.vowel_count(input)
        expected = 3
        self.assertEqual(expected, result)



    # Part 2


    # Part 3


    # Part 4


    # Part 5


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()
