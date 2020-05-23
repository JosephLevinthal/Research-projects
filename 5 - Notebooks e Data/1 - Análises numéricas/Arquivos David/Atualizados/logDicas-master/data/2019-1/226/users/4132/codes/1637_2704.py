

nota = float(input("Digite a nota: "))
bon = input("Digite se S ou N: ")

if(bon.upper() == "S"):
	nota = nota + nota * 0.10

print(nota)