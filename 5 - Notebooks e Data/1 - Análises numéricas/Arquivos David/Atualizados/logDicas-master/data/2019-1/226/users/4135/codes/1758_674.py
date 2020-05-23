# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo
from numpy import*
#leitura de dados:
vet = array(eval(input("vetor:")))
# Qt de elementos
print(size(vet))
#primeiro elemento do vetor
print(vet[0])
#ultimo elemento do vet
print(vet[size(vet)-1])
#maior elemento
print(max(vet))
#menor elemento
print(min(vet))
#soma dos vetores
print(sum(vet))
#media aritmétrica
ma = sum(vet)/size(vet)
print(round(ma,2))
