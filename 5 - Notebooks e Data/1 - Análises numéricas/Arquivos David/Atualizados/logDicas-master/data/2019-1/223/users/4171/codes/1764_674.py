# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import *

v = array(eval(input("v: ")))



print(size(v))
print(v[0])
print(v[size(v)-1])
print(max(v))
print(min(v))
print(sum(v))
print(round(sum(v) / size(v),2))
