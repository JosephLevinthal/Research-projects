from numpy import *
a = float(input("Digite a aceleracao do carro: "))
v0 = float(input("Digite a velocidade inicial do carro: "))
z = int(input("Digite um numero inteiro positivo: "))

t = arange(z) #vetor tempo, comeca no instante zero e vai ate z
d = zeros (z) #vetor contendo apenas zeros de tamanho z
i = 0 #variavel contadora
while(i < z): #o valor de i percorre todas as posicoes do vetor de tamho z
	d[i] = (a*(t[i])**2)/2 + v0*t[i] #para cada posicao t[i] do vetor, e associado um espaco d[i]
	i = i+1 #incremento do laco
print(d) #imprime o vetor contendo as distancias