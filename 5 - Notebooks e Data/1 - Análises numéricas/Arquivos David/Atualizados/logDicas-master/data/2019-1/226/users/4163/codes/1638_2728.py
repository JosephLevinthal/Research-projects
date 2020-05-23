km = float(input("percurso de uma viagem: "))
tp = input("carro A ou B").upper()

if (tp=="A"):
	c = km * 0.125
elif tp=="B":
	c =  km * 1.0
print(round(c, 2))