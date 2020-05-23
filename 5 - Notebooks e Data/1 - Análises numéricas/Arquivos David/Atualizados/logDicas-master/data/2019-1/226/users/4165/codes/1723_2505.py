from math import *
x = eval(input("Insira o angulo: "))
k = int(input("Insira o numero de termos: "))

soma = 0
i = 0
fim = k - i
	
while(k > i):
	soma = soma + ((-1) ** i * (x **(2 *i + 1))) / (factorial (2 * i + 1))
		i = i + 1
print(round(soma, 10))