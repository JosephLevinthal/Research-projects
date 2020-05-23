# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import*
x = array(eval(input("vetor: ")))
qe = size(x)
print(qe)
print(x[0])
print(x[(size(x)-1)])
print(max(x))
print(min(x))
print(sum(x))
print(round((sum(x)/size(x)),2))
#print(size(x))