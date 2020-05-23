# Módulo
from numpy import *
# Entrada
v = array(eval(input("Vetor: ")))
# Acumuladora
soma = 0
# Laço "For"
for i in range(size(v)):
	if (v[i] < 5):
		soma = soma + 1
print(soma)
# Contador do vetor	
cont = zeros(soma, dtype=int)
# Contadores
j = 0
# Laço "for" 02
for i in range(size(v)):
	if (v[i] < 5):
		cont[j] = i
		j = j + 1
# Saída
print(cont)