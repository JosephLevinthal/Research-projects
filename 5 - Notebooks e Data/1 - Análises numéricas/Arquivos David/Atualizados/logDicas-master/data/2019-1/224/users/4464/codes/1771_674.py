from numpy import *

vetor = array(eval(input()))
print(size(vetor))
print(vetor[0])
print(vetor[len(vetor)-1])
print(max(vetor))
print(min(vetor))
print(sum(vetor))
print(round((sum(vetor)/len(vetor)),2))