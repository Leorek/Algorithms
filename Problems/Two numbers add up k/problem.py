"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass? Yes :)

"""

x = [10, 15, 3, 7]
k = 17


def add_up(k, x):

    i = 0
    elements = set()
    found = False
    while not found and i < len(x):
        if elements.__contains__(k - x[i]):
            found = True
            print("Found a match: {} + {} = {}".format(x[i], k - x[i], k))
        else:
            elements.add(x[i])
            i += 1

    if(not found):
        print("There is no match for {}".format(k))

    return found


add_up(k, x)
