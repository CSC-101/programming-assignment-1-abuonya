from types import NoneType

import data

# Representation of a circle.
class Circle:
    # Initialize a new Circle object.
    # input: center as a Point
    # input: radius as a float
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius


    # Provide a developer-friendly string representation of the object.
    # input: Circle for which a string representation is desired.
    # output: string representation
    def __repr__(self) -> str:
        return 'Circle({}, {})'.format(self.center, self.radius)


    # Compare the Circle object with another value to determine equality.
    # input: Circle against which to compare
    # input: Another value to compare to the Circle
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Circle and
                self.center == other.center and
                math.isclose(self.radius, oth

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
# Write your functions for each part in the space below.


# Part 1
# DESIGN RECIPE...
    # Purpose: This function computes and returns the count of the number of vowels (upper and lower) that appear in the input string.
    # Input: string , Output: integer
    # Example Input:  'meow' , Output Given the Input : 2
    # Name of function: vowel_count
    # Me if I was a computer: read through a list, sort out vowels and put them into list, return the length of that list to get how many vowels.

def vowel_count(word: str) -> int:
    split_word = list(word)
    vowel_list = []
    for x in split_word:
        if x == 'e' or x == 'o' or x == 'i' or x == 'u' or x == 'a':
            vowel_list.append(x)
        elif x == 'E' or x == 'O' or x == 'I' or x == 'U' or x == 'A':
            vowel_list.append(x)
    else:
        totalvowels = len(vowel_list)
        print(totalvowels)
        return totalvowels


# Part 2
# DESIGN RECIPE...
    # Purpose: This function takes a nested list and returns a new list containing the elements of the input list that are of length 2.
    # Input: list[list[int]] , Output: list[list[int]]
    # Example Input:  [[1,23,4], [5,6], [78]] , Output Given the Input : [[5,6]]
    # Name of function: short_lists
    # Me if I was a computer: take list, use a list comprehension to filter the length of each nested list, and if its length == 2, append that list into a new list.
def short_lists(input: list[list[int]]) -> list[list[int]]:
    newList = []
    for x in input:
        if len(x) == 2:
            newList.append(x)
    else:
        print(newList)
        return newList

# Part 3
# DESIGN RECIPE...
    # Purpose: This function takes a nested list and returns a new list with the elements of length 2 in ascending order.
    # Input: list[list[int]] , Output: list[list[int]]
    # Example Input:  [[1,23,4], [6,5], [78]] , Output Given the Input : [[5,6]]
    # Name of function: ascending_pairs
    # Me if I was a computer: take list, use a list comprehension to filter the length of each nested list, and if its length == 2, append that list into a new list.
    # Then, filter through the new list, evaluate if the index[0] of a nested list is less/greater than index[1] of that same nested list.
    # Then, change the individual index values of the list to keep the elements in the same order as the resulting list from before.
def ascending_pairs(input: list[list[int]]) ->  list[list[int]]:
    ascending_list = []
    for x in input:
        if len(x) == 2:
            if x[0] > x[1]:
                ascending_list.append([x[1], x[0]])
    else:
        print(ascending_list)
        return ascending_list

# Part 4
# DESIGN RECIPE...
    # Purpose: This function computes and returns the sum of the input prices as a new Price object, but cents is not above 99.
    # Input: integer , Output: float
    # Example Input:  (5, .50) , Output Given the Input : 5.50
    # Name of function: add_prices
    # Me if I was a computer: take two inputs for price (dollars and cents), find the individual total costs for each price (dollars and cents combined),
    # divide by / 100 to get a float value and convert back to dollars and cents, then add the total individual costs to get the sum of both prices.
def add_prices(firstprice: Price, secondprice: Price) -> float:
    total_firstprice = firstprice.dollars + firstprice.cents / 100
    total_secondprice = secondprice.dollars + secondprice.cents / 100
    combinedprices = total_firstprice + total_secondprice
    print(combinedprices)
    return combinedprices

# Part 5
# DESIGN RECIPE...
    # Purpose: This function takes a parameter of Rectangle and returns the area of the provided rectangle.
    # Input: integer , Output: float
    # Example Input:  (7,7) , Output Given the Input : 49
    # Name of function: rectangle_area
    # Me if I was a computer: take the parameter of rectangle, create a variable area that computes the two points of rectangle class times each other.
def rectangle_area(x: Rectangle) -> float:
    area = x.top_left * x.bottom_right
    print(area)
    return area

# Part 6
# DESIGN RECIPE...
    # Purpose: This function takes two parameters of type string and list[Book], returning a list of all books written by the author inputted.
    # Input: str, list[str] , Output: list[str]
    # Example Input:  ("Andy Weir", Book_List) , Output Given the Input : ["The Martian"]
    # Name of function: books_by_author
    # Me if I was a computer: first, i'd create a list of books with authors so I have a list to reference from. Then, I'll filter through the list
    # by each element to see if it matches the inputted author's name. If a result matches, append that element to a new list that contains all books that have that authors' name.

def books_by_author(name: str, books: list[Book]) -> list[str]:
    book_list = []
    for book in books:
        if book.authors == name:
            book_list.append(book.title)
    else:
        return book_list
# Part 7
# DESIGN RECIPE...
    # Purpose: This function takes a parameter of class Rectangle, returning a Circle (another class object) which is a circle that encloses the rectangle.
    # Input: float Output: float
    # Example Input: , Output Given the Input :
    # Name of function: circle_bound
    # Me if I was a computer: i'd first calculate the center of the rectangle, and uhmmmmm
def circle_bound(x: Rectangle) -> Circle:
    calculate_x_center = ()




# Part 8


