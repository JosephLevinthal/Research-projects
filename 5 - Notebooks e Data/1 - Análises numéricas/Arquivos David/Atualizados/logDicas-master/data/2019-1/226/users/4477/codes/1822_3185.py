# Módulo
from numpy import *
# Entrada
v = input("plvra: ")
# Acumulativa
s = ""
# Laço
for i in range(size(v)):
	j = size(v) - i - 1
	s = v[i]
	v[i] = j[i]
	j[i] = s	
	
	
	
	
	
# Saída
print(j)