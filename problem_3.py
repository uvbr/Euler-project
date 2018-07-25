"""The prime factors of 13195 are 5, 7, 13 and 29."""

import math


class Abc(object):

    """The prime factors of 13195 are 5, 7, 13 and 29."""

    def __init__(self):
        pass

    """The prime factors of 13195."""

    def prime_factors(self, number):

        """What is the largest prime factor of the number 600851475143.

        """

        natur = []
        while number % 2 == 0:
            print 2,
            number = number / 2

        for i in range(3, int(math.sqrt(number))+1, 2):

            while number % i == 0:
                natur.append(i)
                number = number / i

        if number > 2:
            print number
        print max(natur)

    """The prime factors of 13195."""

    def prime_actors(self, number):

        """What is the largest prime factor of the number 600851475143.

        """

        while number % 2 == 0:
            print 2,
            number = number / 2

        print number


ABC = Abc()
ABC.prime_factors(600851475143)
