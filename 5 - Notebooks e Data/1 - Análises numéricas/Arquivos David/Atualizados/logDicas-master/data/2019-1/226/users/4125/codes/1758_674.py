# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import*
n = array(eval(input("digite o vetor: ")))
print(size(n))
print(n[0])
print(n[-1])
print(max(n))
print(min(n))
print(sum(n))
print(round(sum(n)/size(n), 2))