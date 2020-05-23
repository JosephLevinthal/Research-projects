# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import *

vet = array(eval(input("vetores: ")))

#qtd de elementos
print(size(vet))

#primeiro elemento
print(vet[0])

#ultimo elemento
print(vet[-1])

#maior elemento
print(max(vet))

#menor elemento
print(min(vet))

#soma dos elementos
print(sum(vet))

#media aritmetica
x = sum(vet) / size(vet)
print(round(x, 2))