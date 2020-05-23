# Módulo
from numpy import *
# Entrada
v = array(eval(input("Numero: ")))
# Variável 1
x = 0
# Laço 1
for i in v:
	if (i % 2) != 0:
		x = x + 1
# Contador do vetor
cont = zeros(x, dtype=int)
# Variável 2
a = 0
b = 0
# Laço 2
for r in v:
	if (r % 2) != 0:
		cont[a] = v[b]
		a = a + 1
	b = b + 1
# Saída
print(cont)