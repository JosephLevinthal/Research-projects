# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import*
a = array(eval(input("vetor: ")))
print(size(a))
print(a[0])
print(a[-1])
print(max(a))
print(min(a))
print(sum(a))
l=(sum(a)/ size(a))
print(round(l,2))
