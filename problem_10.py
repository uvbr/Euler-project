


def problem_10(n):
	sum=0
	l=[]
	for i in range(1,int(n)):
	    for j in range(2,(i+1)):
	        if i%j==0:
	            if i==j:
	                # print(i)
	                sum=sum+i
	                l.append(i)
	                
	            break
	print sum
	print l

problem_10(2000000)