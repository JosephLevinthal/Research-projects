nota = float(input("Digite o valor da nota: "))
bon = input("Bonificao (S/N): ")

if(bon.upper() == "S"):
	nota = nota + (10*nota/100)
print(round(nota,1))