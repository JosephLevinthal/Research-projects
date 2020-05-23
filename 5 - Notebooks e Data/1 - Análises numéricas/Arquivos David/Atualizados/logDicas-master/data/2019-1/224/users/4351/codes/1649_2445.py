escala=input("escala em C ou F : ")
valor=float(input("valor da temp: "))
F=5/9 * (valor - 32)
C=(valor * (9/5) + 32)
escala=escala.upper()
if(escala=="C"):
	print(round(C, 2))
else:
	print(round(F, 2))