from math import*
c = int(input ( "Pontos de vida : "))
D1 =int( input("Numero sorteado: "))
D2=int( input("Numero sorteado: "))

dano= int((sqrt((5 * D1))  + (pi**(D2/3))))

print (c - dano)
