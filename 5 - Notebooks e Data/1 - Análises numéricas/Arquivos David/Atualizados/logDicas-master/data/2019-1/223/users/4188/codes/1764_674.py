# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import *
v=array(eval(input("digite vetor: ")))
a=size(v)
b=(v[0])
c=(v[-1])
d=max(v)
f=min(v)
g=sum(v)
j=sum(v)/size(v)
print(a)
print(b)
print(c)
print(d)
print(f)
print(g)
print(round(j,2))