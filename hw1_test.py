from importlib.metadata import Lookup

import data
import hw1
import unittest

# Abbreviated representation of an employee.
class Employee:
    # Initialize a new Employee object.
    # input: the employee's name as a string
    # input: the employee's pay rate as an integer (for simplicity)
    def __init__(self, name: str, pay_rate: int):
        self.name = name
        self.pay_rate = pay_rate


    # Provide a developer-friendly string representation of the object.
    # input: Employee for which a string representation is desired.
    # output: string representation
    def __repr__(self):
        return "Employee('{}', {})".format(self.name, self.pay_rate)


    # Compare the Employee object with another value to determine equality.
    # input: Employee against which to compare
    # input: Another value to compare to the Employee
    # output: boolean indicating equality
    def __eq__(self, other):
        return (other is self or
                type(other) == Employee and
                self.name == other.name and
                self.pay_rate == other.pay_rate)

# Representation of a book.
class Book:
    # Initialize a new Book object.
    # input: the book's authors as a list of strings
    # input: the book's title as a string
    def __init__(self, authors: list[str], title: str):
        self.authors = authors
        self.title = title


    # Provide a developer-friendly string representation of the object.
    # input: Book for which a string representation is desired.
    # output: string representation
    def __repr__(self):
        return "Book({}, '{}')".format(self.authors, self.title)


    # Compare the Book object with another value to determine equality.
    # input: Book against which to compare
    # input: Another value to compare to the Book
    # output: boolean indicating equality
    def __eq__(self, other):
        return (self is other or
                type(other) == Book and
                self.authors == other.authors and
                self.title == other.title)

# Representation of a two-dimensional point.
class Point:
    # Initialize a new Point object.
    # input: x-coordinate as a float
    # input: y-coordinate as a float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    # Provide a developer-friendly string representation of the object.
    # input: Point for which a string representation is desired.
    # output: string representation
    def __repr__(self) -> str:
        return 'Point({}, {})'.format(self.x, self.y)


    # Compare the Point object with another value to determine equality.
    # input: Point against which to compare
    # input: Another value to compare to the Point
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Point and
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y))

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

# Representation of an axis-aligned rectangle.
class Rectangle:
    # Initialize a new Rectangle object.
    # input: top-left corner as a Point
    # input: bottom-right corner as a Point
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right


    # Provide a developer-friendly string representation of the object.
    # input: Rectangle for which a string representation is desired.
    # output: string representation
    def __repr__(self) -> str:
        return 'Rectangle({}, {})'.format(self.top_left, self.bottom_right)


    # Compare the Rectangle object with another value to determine equality.
    # input: Rectangle against which to compare
    # input: Another value to compare to the Rectangle
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Rectangle and
                self.top_left == other.top_left and
                self.bottom_right == other.bottom_right)

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
        input = Rectangle(7,7)
        result = hw1.circle_bound(input)



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
