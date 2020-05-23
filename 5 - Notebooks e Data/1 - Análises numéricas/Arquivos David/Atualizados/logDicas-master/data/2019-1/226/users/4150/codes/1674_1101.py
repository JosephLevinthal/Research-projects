# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

a = float(input("consumo de energia: "))
b = input("tipo de instalacao: ").upper()

print("Entradas:", a , "kWh" " e tipo" , b , )

r = (round(a*0.44, 2))
r1	= (round(a*0.65, 2))	
c =(round(a*0.55, 2))
c1 = (round(a*0.60, 2))
i = (round(a*0.55, 2))
i1 = (round(a*0.60, 2))

if (b != "R") and (b != "I") and (b != "C"):
	print("Dados invalidos")
else:
	if (a > 0):
		if(a<500) and (b =="R"):
			print("Valor total: R$", r)
		else:
			if(a >= 500) and (b=="R"):
				print("Valor total: R$", r1)
			else:
				if(a <= 1000) and(b=="C"):
					print("Valor total: R$", c)
				else:
					if(a>1000) and (b=="C"):
						print("Valor total: R$", c1)
					else:
						if(a<=5000) and (b == "I"):
							print("Valor total: R$", i)
						else:
							if(a>5000) and( b=="C"):
								print("Valor total: R$", i1)
	else:
		print("Dados invalidos")
	