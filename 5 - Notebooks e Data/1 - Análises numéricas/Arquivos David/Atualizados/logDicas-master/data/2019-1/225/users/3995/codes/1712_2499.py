from math import*
n=int(input("numero:"))
t=1
e=1
while(n>0 and n!=t):
	
	e = e + 1/factorial(t)
	t=t+1
	
print(round(e, 8))