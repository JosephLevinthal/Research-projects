# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import *

V = array(eval(input("Insira um vetor: ")))

print(size(V))
print(V[0])
print(V[-1])
print(max(V))
print(min(V))
print(sum(V))
m = sum(V)/size(V)
print(round(m, 2))