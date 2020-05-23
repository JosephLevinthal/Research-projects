nota = float(input("digite a nota: "))
boni = (input("bonificacao?: ")).upper()
if (boni == "S"):
	men = nota + (nota * 10/100)
else:
	men = nota
print(men)

