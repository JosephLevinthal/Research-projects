# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import*
vetor= array(eval(input("digite numeros:")))
print(size(vetor))
print(vetor[0])
tam= size(vetor)
print(vetor[tam-1])
print(max(vetor))
print(min(vetor))
print(sum(vetor))
media= (sum(vetor)/tam)
print(round(media, 2))