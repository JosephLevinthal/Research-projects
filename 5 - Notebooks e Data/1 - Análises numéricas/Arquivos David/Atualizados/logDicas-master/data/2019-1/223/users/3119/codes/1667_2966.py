m = input("MULHER? S ou N? ")
ingresso = float(input("Valor integral do ingresso: "))
quant = int(input("Quantidade de ingressos: "))

if( m == "S"):
	msg = (ingresso * 0.80) * quant
else:
	msg = ingresso * quant

print(round(msg, 2))