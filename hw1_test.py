from importlib.metadata import Lookup

import data
import hw1
import unittest

# Representation of a price in integer dollars and cents.
class Price:
    # Initialize a new Price object.
    # input: dollars as an integer
    # input: cents as an integer
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents


    # Provide a developer-friendly string representation of the object.
    # input: Price for which a string representation is desired.
    # output: string representation
    def __repr__(self) -> str:
        return 'Price({}, {})'.format(self.dollars, self.cents)


    # Compare the Price object with another value to determine equality.
    # input: Price against which to compare
    # input: Another value to compare to the Price
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Price and
                self.dollars == other.dollars and
                self.cents == other.cents)


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count1(self):
        input = "meow"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)

    def test_vowel_count2(self):
        input = "OMNITRIX"
        result = hw1.vowel_count(input)
        expected = 3
        self.assertEqual(expected, result)

    # Part 2
    def test_short_lists1(self):
        input = [[12,2]]
        result = hw1.short_lists(input)
        expected = [[12,2]]
        self.assertEqual(expected, result)

    def test_short_lists2(self):
        input = [[12,2], [345,6743,6436346,646], [32443,324], [143,1]]
        result = hw1.short_lists(input)
        expected = [[12,2],[32443,324], [143,1]]
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs1(self):
        input = [[1,23,4], [6,5], [32, 29]]
        result = hw1.ascending_pairs(input)
        expected = [[5,6], [29, 32]]
        self.assertEqual(expected, result)

    def test_ascending_pairs2(self):
        input = [[-4, -7], [6,5,34,5], [32,-9]]
        result = hw1.ascending_pairs(input)
        expected = [[-7,-4], [-9, 32]]
        self.assertEqual(expected, result)

    # Part 4
    def test_add_prices1(self):
        input = (Price(5, 50))
        another = (Price(10, 10))
        result = hw1.add_prices(input, another)
        expected = 15.60
        self.assertEqual(expected, result)

    def test_add_prices2(self):
        input = (Price(3, 40))
        another = (Price(4, 45))
        result = hw1.add_prices(input, another)
        expected = 7.85
        self.assertEqual(expected, result)

    # Part 5


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()
