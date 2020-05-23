from math import*
pontos = int(input("Digite os pontos de vida iniciais: "))
d1 = int(input("Digite o valor sortedao do dado: "))
d2 = int(input("Digite o valor sortedao do dado: "))
dano = int(sqrt(5*d1) + (pi)**(d2/3))
print((pontos - dano))