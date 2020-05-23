# Não se esqueça de incluir o módulo numpy
from numpy import *
v = array(eval(input("Digite um vetor : "))) #definicao do vetor
s = size(v) #size e a funcao para definir a qntidade de elementos do vetor
n = s-1 #indice do ultimo elemento do vetor, semelhante a [-1] 
m = sum(v)/s #ou mean e a media, soma dos valores, div pela quantdade de elementos
print(size(v)) 
print(v[0]) #imprime o primeiro elemento
print(v[n]) #imprime o ultimo elemento = [-1]
print(max(v)) #imprime o valor maximo
print(min(v)) #imprime o valor minimo
print(sum(v)) # imprime  soma
print(round(m, 2)) #imprime a 