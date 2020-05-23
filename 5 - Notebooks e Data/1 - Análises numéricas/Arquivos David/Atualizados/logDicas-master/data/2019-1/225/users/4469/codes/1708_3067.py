ataque = input().upper()
d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())

if((d1 < 1 or d1 > 6) or (d2 < 1 or d2 > 6) or (d3 < 1 or d3 > 6) or (d4 < 1 or d4 > 6)) or (ataque != "ESPADA" and ataque != "CAUDA"):
	print("Entrada invalida")
elif(ataque == "ESPADA"):
	print((d1 + 6) + (d2 + 6) + (d3 + 6) + (d4 + 6))
else:
	print((d1 + d2 + d3) * d4)