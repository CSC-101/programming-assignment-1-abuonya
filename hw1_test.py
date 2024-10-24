from importlib.metadata import Lookup
import hw1
import unittest
from data import Employee
from data import Book
import math
from data import Point
from data import Price
from data import Rectangle
from data import Circle

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
    def test_rectangle_area1(self):
        input = (Rectangle(7,7))
        result = hw1.rectangle_area(input)
        expected = 49
        self.assertEqual(expected, result)

    def test_rectangle_area2(self):
        input = (Rectangle(12,12))
        result = hw1.rectangle_area(input)
        expected = 144
        self.assertEqual(expected, result)

    # Part 6
    def test_books_by_author1(self):
        book1 = (Book("Andy Weir", "The Martian"))
        book2 = (Book("Toni Morrison", "A Mercy"))
        book_list = [book1, book2]
        input = "Andy Weir"
        result = hw1.books_by_author(input, book_list)
        expected = ["The Martian"]
        self.assertEqual(expected, result)

    def test_books_by_author2(self):
        book1 = (Book("Andy Weir", "The Martian"))
        book2 = (Book("Toni Morrison", "A Mercy"))
        book3 = (Book("Andy Weir", "Project Hail Mary"))
        book_list = [book1, book2, book3]
        input = "Andy Weir"
        result = hw1.books_by_author(input, book_list)
        expected = ["The Martian", "Project Hail Mary"]
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_bound1(self):
        input = Rectangle([7],[7])
        result = hw1.circle_bound(input)
        expected = ((3.5, 3.5), 4.9497)
        self.assertEqual(expected, result)

    # Part 8
    def test_below_pay_average(self):
        employee1 = Employee("Jericho", 425)
        employee2 = Employee("John", 700)
        employee3 = Employee("Charles", 700)
        employee4 = Employee("JoAnne", 400)
        list_of_employees = [employee1, employee2, employee3, employee4]
        result = hw1.below_pay_average(list_of_employees)
        expected = ["Jericho", "JoAnne"]
        self.assertEqual(expected, result )

    def test_below_pay_average2(self):
        employee1 = Employee("Jericho", 0)
        employee2 = Employee("John", 700)
        employee3 = Employee("Charles", 700)
        employee4 = Employee("Charles Jr.", 100000)
        employee5 = Employee("JoAnne", 0)
        list_of_employees = [employee1, employee2, employee3, employee4, employee5]
        result = hw1.below_pay_average(list_of_employees)
        expected = ["Jericho", "John",  "Charles", "JoAnne"]
        self.assertEqual(expected, result )


if __name__ == '__main__':
    unittest.main()
