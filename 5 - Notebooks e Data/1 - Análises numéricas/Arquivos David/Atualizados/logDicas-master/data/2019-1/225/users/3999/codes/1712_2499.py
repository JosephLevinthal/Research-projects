from math import*
k=int(input())
e=0
i=0
while(i<k):
	e=e+(1/factorial(i))
	i=i+1
print(round(e,8))	