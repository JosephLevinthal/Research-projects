valor = float(input("digite valor: "))
#total = valor + gorjeta

#gorjeta1 = valor*0.1
#gorjeta2 = valor*0.09
#gorjeta3 = valor*0.08
#gorjeta4 = valor*0.07

if(valor >= 0 and <= 100):
	mensagem = valor * 0.1
else:
	if(valor > 100 and valor <= 200):
		mensagem = valor * 0.09
	else:
		if(valor > 200 and valor <= 300):
			mensagem = valor * 0.08
		else:
			if(valor > 300):
				mensagem = valor * 0.07

total = mensagem + valor

				
print(round(total, 2)