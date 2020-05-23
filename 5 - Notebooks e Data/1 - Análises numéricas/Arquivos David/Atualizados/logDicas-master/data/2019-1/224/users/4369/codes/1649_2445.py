t = input("Digite C ou F: ")
vT = float(input("Digite o valor da temperatura: "))
F = 5/9 * (vT - 32)
C = (vT * (9/5) + 32)
if(t.upper() == "C"):
	print(round(C, 2))
else:
	print(round(F, 2))

