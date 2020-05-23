from math import *
x= float(input("numero real:"))
k= int(input("numero de termos:"))
t=1
n=0

while(-1 < x < +1) and (k>0):
	t=t+2
	x1=((x**t)/factorial(t))
	
print(round(x,7))