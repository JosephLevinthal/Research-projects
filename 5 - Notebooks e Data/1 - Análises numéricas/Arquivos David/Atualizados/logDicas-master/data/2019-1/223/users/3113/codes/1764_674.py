# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import*
n=array(eval(input("")))

a=size(n)
b=n[0]
c=n[-1]
d=max(n)
e=min(n)
f=sum(n)
g=round(sum(n)/size(n),2)

print(a,b,c,d,e,f,g)