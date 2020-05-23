from numpy import*
v = array(eval(input("Tipo de espada: ")))
n = array(eval(input("Nivel: ")))
i = 0
dano = 0
while (i < size(v)):
	if (v[i] == "CENOURA"):
		dano = dano + (2 * n[i])
	elif (v[i] == "FERRO"):
		dano = dano + (4 * n[i])
	elif (v[i] == "DWARVEN"):
		dano = dano + (8 * n[i])
	elif (v[i] == "ELVEN"):
		dano = dano + (11 * n[i])
	elif (v[i] == "DAEDRIC"):
		dano = dano + (14 * n[i])
	i = i + 1
print(dano)