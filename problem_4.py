

def problem4():
	l=[]
	for i in range(100,1000):
		for j in range(100,1000):
			prod=i*j
			rev_num=reverse_number(prod)
			if prod==rev_num:
				l.append(prod)
	print max(l)

def reverse_number(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n /= 10
    return r



problem4()