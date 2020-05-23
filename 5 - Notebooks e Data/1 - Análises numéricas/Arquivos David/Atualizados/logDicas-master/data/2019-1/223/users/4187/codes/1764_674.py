# Não se esqueça de1, incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import*
vet = array(eval(input("vet:")))

print(size(vet))
print(vet[0])
print(vet[size(vet)-1])#vet[-1]
print(max(vet))
print(min(vet))
print(sum(vet))
#print(round(sum(vet)/size(vet),2))
print(round(mean(vet),2))