# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import*
v = array(eval(input("Insira um vetor: ")))

#Quant elemento
print(size(v))

#Primeiro elmento
print(v[0])
#Ultimo elemento
print(v[-1])
#Maior elemento
print(max(v))
#Menor elemento
print(min(v))
#Soma dos elementos
print(sum(v))
#Media dos elementos
print(round(sum(v) / size(v), 2))