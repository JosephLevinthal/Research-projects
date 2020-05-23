from math import*
x= eval(input("qual seu angulo? "))
k= int(input("qual seu termo geral? "))
t=0
s=0
while (t<k):
	s= s + ((x**(2*t +1)/factorial(2*t+1)))*(-1)**t
	t=t+1
print(round(s,10))