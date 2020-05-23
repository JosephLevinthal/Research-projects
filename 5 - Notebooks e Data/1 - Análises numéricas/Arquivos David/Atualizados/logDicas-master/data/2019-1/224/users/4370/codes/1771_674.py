# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import *
V=eval(input("digite o vetor: "))
print(size(V))
print(V[0])
print(V[-1])
print(max(V))
print(min(V))
print(sum(V))
media=sum(V)/size(V)
print(round(media,2))


