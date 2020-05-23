from math import*
x = float(input("insira uma numero: "))
k = int(input("quantidade de termos: "))

soma = 0
i = 0


while(i<k):
	soma = soma + (x**i)/ factorial(1*i)
	i =i+1
print(round(soma, 9))
