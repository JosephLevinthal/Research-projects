x = float(input("valor da nota: "))
b = input("bonificacao: ")
S = x

if (b.upper() == "S"):
	msg = S * 110 / 100
else:
	msg = x

print(msg)