from numpy import*
v1 = array(eval(input("gols feitos/partida: ")))
v2 = array(eval(input("gols do adversario/partida: ")))
v3 = zeros(3, dtype=int)
y = 0
empate = 0
derrota = 0
vitoria = 0
for x in v1:
	if x == v2[y]:
		empate = empate + 1
	elif x<v2[y]:
		derrota = derrota + 1
	elif x > v2[y]:
		vitoria = vitoria + 1
	y = y + 1
v3[0] = vitoria
v3[1]	= empate
v3[2] = derrota
print(v3)