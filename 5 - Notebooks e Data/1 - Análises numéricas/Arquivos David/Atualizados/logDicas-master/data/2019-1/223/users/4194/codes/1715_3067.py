ataque = input("Tipo de ataque: ESPADA ou CAUDA? ").upper()
d1 = int(input("Jogada 1: "))
d2 = int(input("Jogada 2: "))
d3 = int(input("Jogada 3: "))
d4 = int(input("Jogada 4: "))
esp = (d1+6) + (d2+6) + (d3+6) + (d4+6)
cau = ((d1 + d2 + d3) * d4)

if(((d1<1) or (d1>6) or (d2<1) or (d2>6) or (d3<1) or (d3>6) or (d4<1) or (d4>6)) or (ataque != "ESPADA") or (ataque != "CAUDA")):
	print("Entrada invalida")
elif(ataque == "CAUDA"):
	print(cau)
elif(ataque == "ESPADA"):
	print(esp)