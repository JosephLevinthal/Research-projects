consumo = float(input("consumo de agua: "))

funcao = consumo*3 + 30
funcao2 = (consumo*3.5) + 30

if  (consumo < 10):
     print(round(funcao, 2))
		
else:
	 print(round(funcao2, 2))