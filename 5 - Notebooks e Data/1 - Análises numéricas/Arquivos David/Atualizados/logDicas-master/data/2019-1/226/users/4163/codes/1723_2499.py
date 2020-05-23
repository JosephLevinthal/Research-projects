from math import*
k= int(input(""))


s=0
i=0
f=k-1

while(i<=f):
	s = s + 1 /factorial(i)
	i = i +1
	
print(round(s,8))