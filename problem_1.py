
"""The sum of all the multiples of 3 or 5 below 1000."""


def function_foo(number):

    """List all the natural numbers below 10 that are multiples of3 or 5.
    we get 3, 5, 6 and 9.The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.

    """

    j = 0
    nat_ur = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            j = j + i
            nat_ur.append(i)
    print j

function_foo(1000)
