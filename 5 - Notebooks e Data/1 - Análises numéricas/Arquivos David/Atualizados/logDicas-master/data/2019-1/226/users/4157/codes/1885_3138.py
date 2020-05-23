from numpy import*
n = array(eval(input("n :")))
for x in(n):
	m = ((n[0]**7+n[1]**7+n[x-1]**7)/x)**1/7
print(round(m, 2))