# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import*
v=array(eval(input("Digite o numero: ")))
print(size(v)) #1 quantidade de elemento do vetor
print(v[0]) #2 primeiro elemento do vetor
print(v[4]) #3 ultimo elemento do vetor
print(max(v)) #4 Maior elemento do vetor
print(min(v)) #5 Menor elemento de vetor
print(sum(v)) #6 soma dos elementos do vetor
x=sum(v)/size(v) #Media aritmética
print(round(x, 2))