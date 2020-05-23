# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import*
v1=array(eval(input("digite os vetores: ")))
print(size(v1))
print(v1[0])
print(v1[-1])
print(max(v1))
print(min(v1))
print(sum(v1))
media=sum(v1)/size(v1)
print(round(media,2))