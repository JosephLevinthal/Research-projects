from math import*
k=int(input("digite um numero natural: "))
e=1
i=1
while(i<k):
	e=e+(1/factorial(i))
	i=i+1
print(round(e, 8))