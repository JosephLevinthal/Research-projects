from math import*

x = abs(eval(input("digite o angulo em radianos: ")))
k = abs(int(input("digite o numero de termos da serie: ")))
i = 0
j = 0
soma = 0
while(k>0)and(x>=0):
	soma = soma + ((((x)**j)/(factorial(i)))*((-1)**j))
	i = i + 2
	j = j + 1
	k = k - 1
print(round(soma,6))