from types import NoneType

import data

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
    # Me if I was a computer: take two inputs for price (dollars and cents), find the costs for each price in dollars, then the sum for each price in their cents.
    #

def add_prices(firstprice: Price, secondprice: Price) -> float:
    total_dollars = firstprice.dollars + secondprice.dollars
    total_cents = firstprice.cents + secondprice.cents
    total_price = total_dollars + total_cents
    print(total_price)
    return total_price



# Part 5


# Part 6


# Part 7


# Part 8


