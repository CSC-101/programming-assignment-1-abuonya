from types import NoneType

import data

# Write your functions for each part in the space below.


# Part 1
# DESIGN RECIPE...
    # Purpose: This function computes and returns the count of the number of vowels (upper and lower) that appear in the input string.
    # Input: string , Output: integer
    # Example Input:  'meow' , Output Given the Input : 2
    # Name of function: vowel_count
    # read through a list, sort out vowels and put them into list, return the length of that list to get how many vowels

def vowel_count(word: str) -> int:
    split_word = list(word)
    vowel_list = []
    for x in split_word:
        if x == 'e' or x == 'o' or x == 'i' or x == 'u' or x == 'a':
            vowel_list.append(x)
    else:
        totalvowels = len(vowel_list)
        print(totalvowels)
        return totalvowels


# Part 2


# Part 3


# Part 4


# Part 5


# Part 6


# Part 7


# Part 8


