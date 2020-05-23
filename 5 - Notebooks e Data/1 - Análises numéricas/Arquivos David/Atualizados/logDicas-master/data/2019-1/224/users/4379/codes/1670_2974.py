qtdg=float(input("a quantidade de acai no copo:"))
qtds=int(input("a quantidade de salgados:"))
valor=float(input("o valor pago:"))
qtg1= 24
sal= 3

total= sal*qtds + qtdg *qtg1
print(round(total, 2))
if valor>total:
	print("Sim")
else:
    print("Nao")
	