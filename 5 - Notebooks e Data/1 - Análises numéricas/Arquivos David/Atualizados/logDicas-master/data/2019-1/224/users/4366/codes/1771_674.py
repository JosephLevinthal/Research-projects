# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import*
vet=array(eval(input("digite um vetor:")))
#quantidade de elementos do vetor
print(size(vet))
#primeiro elemento
print(vet[0])
#ultimo elemento
print(vet[-1])
#maior elemento
print(max(vet))
#menor elemento
print(min(vet))
#soma dos elementos
print(sum(vet))
#media aritmetica dos elementos
print(round(sum(vet)/size(vet),2))




