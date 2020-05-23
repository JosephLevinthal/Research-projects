# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import*

bb = array(eval(input("Digite :")))
print (size(bb))
print (bb[0])
print (bb[-1])
print (max(bb))
print (min(bb))
print (sum(bb))
print(round(sum(bb)/size(bb), 2))