from numpy import *

Vetor1 = array(eval(input("digite vetor1:")))
Vetor2 = array(eval(input("digite vetor2:")))

vet_mes = array(["janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"])

i = 0
maior = max(Vetor1)

while(Vetor1[i] != maior):
	i = i + 1

print(i + 1)