from numpy import *
a = float(input("aceleracao:"))
v = float(input("velocidade inicial:"))
N = int(input("numero inteiro:"))
vetor=arange(N)
carlos=((a*vetor**2)/2)+v*vetor
print(carlos)