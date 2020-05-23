# Não se esqueça de incluir o módulo numpy
from numpy import *
# Use o navegador Chrome, para copiar/colar a entrada de exemplo # NÃO ENTENDI PRA QUE USAR O CROMER
vetor = array(eval(input("vetores: ")))
# Quantidade de elementos do vetor
print(size(vetor))
# Primeiro elemento do vetor
print(vetor[0])
# Último elemento do vetor
print(vetor[4])
# Maior elemento do vetor
print(max(vetor))
# menor elemento do vetor
print(min(vetor))
# Soma dos elementos do vetor
print(sum(vetor))
# Média aritmética dos elementos do vetor
media = sum(vetor)/size(vetor)
print(round(media,2))
		