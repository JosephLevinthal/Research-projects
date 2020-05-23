# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import*
v = array(eval(input("Digite um vetor: ")))

#Quant. de elementos
print(size(v))

#Primeiro elemento
print(v[0])

#Ultimo elemento
print(v[-1])

#Maior elemento
print(max(v))

#Menor elemento
print(min(v))

#soma dos elementos
print(sum(v))

#Média dos elementos
print(round(sum(v) / size(v), 2))
