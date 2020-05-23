# Modulo numpy
from numpy import *
# Entradas
g = array(eval(input("digite o valor: ")))
# Variavel
i = 0
cont = 0
# Laço
while i <size(g):
	if g[i] > 99:
		print(i)
		cont = cont + 1
	i = i + 1
# Saida
print(cont)