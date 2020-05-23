# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import *
vet = array(eval(input("valor:")))
print(size(vet))
print(vet[0])
print(vet[-1])
print(max(vet))
print(min(vet))
print(sum(vet))

media= (sum(vet)/size(vet))
print(round(media,2))

