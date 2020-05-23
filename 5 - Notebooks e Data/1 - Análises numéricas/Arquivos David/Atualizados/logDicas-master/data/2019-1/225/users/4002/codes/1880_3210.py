string = input(" ")
string = string.split(",")
nota = [ ]

for i in range(len(string)):
	aux = float(input(""))
	nota.append(aux)

maior = 0 

for i in range(len(nota)):
	if nota[i] > nota[maior]:
		maior = i
print("O aluno que possui a maior nota e o aluno", string[maior])