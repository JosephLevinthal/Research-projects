from math import*
n= int(input("qual seu termo geral? "))
i=2
s=3
t=0
while(n>1):
	s=s+(4/(i*(i+1)*(i+2)))*(-1)**t
	i=i+2
	t=t+1
	n=n-1
print(round(s,8))