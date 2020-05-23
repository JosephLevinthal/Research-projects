# Módulo
from numpy import *
# Entrada
a = input("Texto: ")
# Laço
for x in a:
	a = a.replace("a","")
	a = a.replace("A","")
# Saída
print(a)