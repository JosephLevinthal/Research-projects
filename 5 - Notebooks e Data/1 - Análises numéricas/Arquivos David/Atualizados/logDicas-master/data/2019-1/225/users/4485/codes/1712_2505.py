from math import *
x= eval(input("angulo:"))
k= int(input("termos:"))
t=0
s=1
n=1
y=0
while (-pi<=x) and (x<=+pi) and (t<k):
	t=t+1
	y=y+(x**n/factorial(n))*s
	n=n+2
	s=s*(-1)
print(round(y,10))