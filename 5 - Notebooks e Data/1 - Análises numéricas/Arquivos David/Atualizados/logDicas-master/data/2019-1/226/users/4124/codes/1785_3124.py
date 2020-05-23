from numpy import *
vet = array(eval(input("Numeros positivos: ")))
i = 0
mt = 1
n = size(vet)
while(i < n-1):
	mt = mt * vet[i] * vet[i + 1]
	i = i + 2
media = mt ** (n ** -1)
print(round(media, 2))
