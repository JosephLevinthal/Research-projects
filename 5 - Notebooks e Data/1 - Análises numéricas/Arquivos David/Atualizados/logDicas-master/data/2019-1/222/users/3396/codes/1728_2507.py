

quant_p = int(input("Digite :"))
perc = int(input("Digite :"))
soma = quant_p
mes = 0
ret = 0

while soma > 0 and soma < 8000:
	ret = int(input("Digite: "))
	soma = soma + (soma * (perc / 100)) - ret
	mes = mes + 1

if soma < ret :
	print("ZERO")
	print(mes)
else:
	print("MAXIMO")
	print(mes)