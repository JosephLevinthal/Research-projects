from numpy import *

a = float(input("Aceleracao: "))
v0 = float(input("Velocidade inicial: "))
n = int(input("N: "))

t = array(arange(n))
vet = zeros(len(t))
cont = 0

while(cont <= t[-1]):
	vet[cont] = ((a * t[cont]**2)/2) + v0 * t[cont]
	cont += 1
					 
print(vet)