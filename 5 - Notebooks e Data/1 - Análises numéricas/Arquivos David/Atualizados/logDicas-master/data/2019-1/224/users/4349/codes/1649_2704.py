a = float(input("nota: "))
bonificacao = input("S/N")

if (bonificacao.upper()) == "S":
	a = a + a*0.10

else:
	a = a
print(a)