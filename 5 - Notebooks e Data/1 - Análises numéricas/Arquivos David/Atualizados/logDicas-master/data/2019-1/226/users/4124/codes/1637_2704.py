nota = float(input("Insira a nota: "))
bon = input("Recebera a bonificacao? (S/N): ").upper()
if(bon == "S"):
	total = (nota + ((10/100) * nota))
else: 
	total = nota
print(total)