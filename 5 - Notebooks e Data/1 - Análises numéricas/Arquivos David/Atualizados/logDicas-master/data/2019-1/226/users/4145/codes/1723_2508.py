from math import*
n =int(input("numero natural: "))
s = 3
i = 2
j=0
while(n>1):
	s= s + (4/(i*(i+1)*(i+2)))*(-1)**j
	i= i+2
	j= j+1
	n= n-1
print(round(s,8))	