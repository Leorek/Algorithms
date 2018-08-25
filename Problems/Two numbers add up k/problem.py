"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""

x = [10, 15, 3, 7]
k = 17


def add_up(k, x):

    i = 0
    found = False
    while not found and i < len(x):
        numberToFind = k - x[i]
        if contains(numberToFind, i + 1, x):
            found = True
            print("Found a match: {} + {} = {}".format(x[i], numberToFind, k))
        else:
            i += 1
    return found


def contains(n, i, x):
    contains = False
    while not contains and i < len(x):
        if x[i] == n:
            contains = True
        else:
            i += 1
    return contains


add_up(k, x)
