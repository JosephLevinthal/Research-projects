from math import*

vida = float(input("Vida Inicial: "))
dado1 = float(input("Dado 1: "))
dado2 = float(input("Dado 2: "))

dano = float(sqrt(5 * dado1) + (pi * (dado2 / 3)))
#restante = int(vida -dano)

print (int(vida - dano))

