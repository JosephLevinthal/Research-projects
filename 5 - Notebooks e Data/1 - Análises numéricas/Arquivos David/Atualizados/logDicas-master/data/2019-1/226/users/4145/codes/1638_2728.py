d = float(input("distancia percorrida: "))
tc = input("tipo de carro: ")

if(tc == "A"):
	con = d/8
else:
	con = d/12
print(con)