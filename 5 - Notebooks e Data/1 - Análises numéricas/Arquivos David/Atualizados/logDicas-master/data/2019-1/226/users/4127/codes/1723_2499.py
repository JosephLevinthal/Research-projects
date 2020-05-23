from math import*
k= int(input("qual seu termo geral? "))
t=0
s=0
while (t<k):
	s= s + (1/factorial(t))
	t=t+1
	
print(round(s,8))