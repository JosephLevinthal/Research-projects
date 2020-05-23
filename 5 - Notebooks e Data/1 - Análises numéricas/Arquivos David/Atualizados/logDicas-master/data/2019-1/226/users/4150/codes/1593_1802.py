from math import*

p = int(input("pontos de vida: "))
d1 = int(input("pimeiro valor:"))
d2 = int(input("segundo valor: "))

dano = (int(sqrt((5*d1)) + (pi**(d2/3))))

pr = p - dano
print(int(pr))