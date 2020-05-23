from numpy import *
x = array(eval(input("Vetor de numeros reais: ")))
soma = 1
m = sum(x) / size(x)
n = size(x)
for i in range(size(x)):
	soma = soma * abs(x[i] - m)
p = (soma) ** (1/n)
print(round(p, 3))