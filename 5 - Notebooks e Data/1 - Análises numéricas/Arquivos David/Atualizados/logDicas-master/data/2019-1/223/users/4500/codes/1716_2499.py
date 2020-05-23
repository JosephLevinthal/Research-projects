from math import*

x = int(input( "digite um numero k:  "))

e = 1

i = 1

while(i < x):
	e = e + (1/factorial(i))
	i = i+1
print(round(e,8))