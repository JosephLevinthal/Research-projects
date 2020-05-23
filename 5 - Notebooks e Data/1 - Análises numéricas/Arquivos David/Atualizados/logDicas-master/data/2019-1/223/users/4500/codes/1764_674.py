# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo
from numpy import*

# Vetor inserido pelo usuário
vet0 = array(eval(input("Vet0: ")))
# Quantidade de elementos do vetor?
print(size(vet0))
# Primeiro elemento do Vetor
print(vet0[0])
# Último elemento do Vetor
print(vet0[size(vet0)-1])
# Maior elemento do Vetor
print(max(vet0))
# Menor elemento do Vetor
print(min(vet0))
# Soma dos elementos do Vetor
print(sum(vet0))
# Média aritmética dos elementos do Vetor
media = (sum(vet0) / size(vet0))
print(round(media, 2))