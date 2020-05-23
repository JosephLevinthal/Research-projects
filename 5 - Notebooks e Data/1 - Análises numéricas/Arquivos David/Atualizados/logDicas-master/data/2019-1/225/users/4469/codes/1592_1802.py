import math

vida_inicial = int(input("Pontos de vida iniciais: "))
d1 = int(input("Primeiro valor sorteado: "))
d2 = int(input("Segundo valor sorteado: "))

dano = int(((5 * d1) ** (1 / 2)) + ((math.pi) ** (d2 / 3)))

vida_restante = vida_inicial - dano

print(vida_restante)