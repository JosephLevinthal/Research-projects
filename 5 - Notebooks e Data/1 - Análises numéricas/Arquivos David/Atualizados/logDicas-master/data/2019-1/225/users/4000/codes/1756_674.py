# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import*
v = array(eval(input("Qual o vetor: ")))
print(size(v))
print(v[0])
print(v[-1])
print(max(v))
print(min(v))
print(sum(v))
t =(sum(v) / size(v))
print(round(t , 2))
