def problem23(n):
	l=[]
	for i in range(1,n+1):
		a=[]
		for j in range(1,i):
			if i%j==0:
				a.append(j)
		if sum(a)>i:
			l.append(i)
	print l

problem23(28123)