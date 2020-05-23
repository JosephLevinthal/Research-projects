from math import * 

vida = float(input("Vida inicial dos monstros: "))
				 
d1 = int(input("Numero do dado 1: "))
d2 = int(input("Numero do dado 2: "))
				 
dano = abs((5 * d1) ** 0.5 + pi ** (d2 / 3))
				 
danototal = int(dano)
			 
print(vida - danototal)