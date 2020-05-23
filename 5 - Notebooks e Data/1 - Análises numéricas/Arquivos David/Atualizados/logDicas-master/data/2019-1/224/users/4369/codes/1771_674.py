# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import*
v = array(eval(input("v: ")))
qe = size(v)
pri = v[0]
ul = v[-1]
maior = max(v)
menor = min(v)
soma = sum(v)
ma = sum(v) / qe
print(qe)
print(pri)
print(ul)
print(maior)
print(menor)
print(soma)
print(round(ma, 2))


