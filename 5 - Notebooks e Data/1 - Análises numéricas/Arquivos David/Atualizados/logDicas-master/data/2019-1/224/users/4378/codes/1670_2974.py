qtdg=float(input("quantidade de acai em gramas:"))
qtds=int(input("quantidade de salgados:"))
valor=float(input("valor pago:"))
qtdg1= 24
sal= 3
x= qtdg/1000
tot= sal * qtds + x * qtdg1
print(round(tot, 2))
if valor>tot:
	print("Sim")
else:
	print("Nao")