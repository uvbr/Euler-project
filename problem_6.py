# Find the difference between the sum of the squares of the
 # first one hundred natural numbers and the square of the sum.


def sum_of_square(n):

	a = (n*(n+1)*((2*n)+1))/6

	return a

def square_of_sum(n):

	b = (n*(n+1)/2)**2
	
	return b 

n=100

print square_of_sum(n)-sum_of_square(n)

