from math import*
vida = int(input("Digite a vida inicial: "))
d1 = int(input("digite um valor de 1 a 20: "))
d2 = int(input("digite um valor de 1 a 20: "))
dano = int((5*d1)**(1/2) + pi**(d2/3))
final = vida - dano
print(final)