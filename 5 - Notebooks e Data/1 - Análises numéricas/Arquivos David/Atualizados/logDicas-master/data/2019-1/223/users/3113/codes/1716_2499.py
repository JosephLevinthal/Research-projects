from math import*
k=int(input("numero natural:"))
t=0
y=0
while(t<k):
	e=(1/factorial(t))
	y=y+e
	t=t+1
	print(factorial(t))
print(round(y,8))