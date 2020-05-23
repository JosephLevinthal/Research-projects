# Nome: Nathaly Barbosa Leite
# Curso: Estatística
# Matrícula: 21954721

from numpy import *

vetor = array(eval(input("Informe o conjunto de numeros: ")))

#vetor = (vetor)

# Quantidade de elementos do vetor
print(size(vetor))

# Primeiro elemento do vetor
print(vetor[0])

# Ultimo elemento do vetor
print(vetor[-1])

# Maior elemento do vetor
print(max(vetor))

# Menor elemento do vetor
print(min(vetor))

# Soma dos elementos do vetor
print(sum(vetor))

# Media aritmetica dos elementos do vetor, com até duas casas decimais de precisão. 
print(round(sum(vetor) / size(vetor),2))
#print (round(mean(vetor)))
