from math import factorial
n=int(input("valor_inicial: "))
c=n
while(n>0):
	i=(1)/(factorial(n))+i
	n=n-i
print(round(n,8))