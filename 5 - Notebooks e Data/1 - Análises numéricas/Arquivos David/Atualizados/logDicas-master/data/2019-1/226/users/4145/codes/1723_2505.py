from math import*
x = eval(input("valor do angulo em radianos: "))
k = int(input("quantidade de repeticoes: "))
s = 0
i=0
while(k>i):
	s = s + ((x**(2*i+1))/factorial(2*i+1))*((-1)**i)
	i= i+1
	
	
print(round(s,10))	