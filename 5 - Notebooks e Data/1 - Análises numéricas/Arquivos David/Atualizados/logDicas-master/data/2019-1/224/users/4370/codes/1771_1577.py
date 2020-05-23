from numpy import *
a = float(input("digite a aceleracao: "))
vo = float(input("digite a velocidade inicial: "))
N = int(input("tempo em funcao do termo N: "))
vetor_t = arange(N,dtype = float)
vetor_d = ((((vetor_t)**2)*a)/2) + vo*vetor_t
print(vetor_d)