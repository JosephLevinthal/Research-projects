from numpy import *

vet = array(eval(input("Vetor: ")))

print(len(vet))
print(vet[0])
print(vet[-1])
print(max(vet))
print(min(vet))
print(sum(vet))
print(round(sum(vet)/len(vet),2))