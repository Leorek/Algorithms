"""
Recursive Staircase problem

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.

Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""
n = 4  # Number of steps
x = {1, 3, 5}  # Number of steps climbable at a time


def num_ways(n, x):
    return num_ways_helper(n, x, [])


def num_ways_helper(n, x, path):
    if n == 0:
        return 1

    ways = 0
    for i in x:
        if i == n:
            ways += 1
            path.append(i)
            print(path)
            path.pop()
        elif i < n:
            path.append(i)
            ways += num_ways_helper(n - i, x, path)
            path.pop()

    return ways


print(num_ways(n, x))
