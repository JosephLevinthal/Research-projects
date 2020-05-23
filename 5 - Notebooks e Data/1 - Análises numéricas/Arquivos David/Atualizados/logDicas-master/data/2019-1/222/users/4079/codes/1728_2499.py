from math import*
termo=int(input("termo geral: "))

i=0
s= 1

while(i < termo-1):
	i=i+1
	s=s+1/factorial(i)
	
print(round(s,8))