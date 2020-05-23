# Modulo d
from numpy import *
# Entradas
vet = array(eval(input("Vetor: ")))
# Saídas
print(size(vet))          # Total de elemntos do vetor
print(vet[0])             # Primero elemento do  vetor
print(vet[-1])            # Ultimo elemento do vetor
print(max(vet))           # Maior elemento do vetor
print(min(vet))           # Menor elemento do vetor
print(sum(vet))           # Soma dos elementos do vetor

# Variavel da media
m = sum(vet)/size(vet)
# Saida (Media)
print(round(m, 2))