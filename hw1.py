from types import NoneType
from data import Employee
from data import Book
import math
from data import Point
from data import Price
from data import Rectangle
from data import Circle

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
    # Example Input: (7,7) , Output Given the Input :((3.5, 3.5), 4.9497)
    # Name of function: circle_bound
    # Me if I was a computer: i'd first calculate the center of the rectangle, find the radius of the circle using a^2+b^2 = c^2 (making a triangle) using rectangle points.
    #
def circle_bound(points: Rectangle) -> Circle:
    calculate_x_center = points.top_left[0] - points.bottom_right[0] / 2 # find coordinate "x" for center point of rectangle
    calculate_y_center = points.top_left[0] - points.bottom_right[0] / 2 # find coordinate "y" for center point of rectangle
    # compile x and y into one coordinate
    center_coordinates = (calculate_x_center, calculate_y_center)

    # find the radius of the circle (it is the same as the length from the center of the rectangle to one of its corners.)
    circle_radius = math.sqrt((calculate_x_center**2) + (calculate_y_center**2))
    circle_coordinates = Circle(center_coordinates, round(circle_radius, 4))
    print(circle_coordinates)
    print(circle_coordinates.radius)
    return circle_coordinates


# Part 8
# DESIGN RECIPE...
    # Purpose: This function takes one parameter of type list[Employee] and returns a llist of the names of employees being paid less than average.
    # Input: list[str] Output: list[str]
    # Example Input: ["Sarah", "Jackson", "Conrad", "Jericho"], Output Given the Input : ["Sarah", "Jericho"]
    # Name of function: below_pay_average
    # Me if I was a computer: first, i'd get a list of all the employees. Go through the list to find all their pay, then take the average of all those numbers.
    # Then, I'd take the same list of employees and filter out if an employee's pay is less than the average pay, appending that employee's name to a new list.
def below_pay_average(allemployees: list[Employee]) -> list[str]:
    #first find total pay...
    underpaid_list = []
    total_employee_pay = 0
    count = 0 # for how many employees there are --> to divide by total sum of pay
    for employee in allemployees:
        total_employee_pay += employee.pay_rate
        count += 1
    # compute average pay...
    average_pay = total_employee_pay / count
    # create list of employees that are underpaid
    for employee in allemployees:
        if employee.pay_rate < average_pay:
            underpaid_list.append(employee.name)
    else:
        print(underpaid_list)
        return underpaid_list



