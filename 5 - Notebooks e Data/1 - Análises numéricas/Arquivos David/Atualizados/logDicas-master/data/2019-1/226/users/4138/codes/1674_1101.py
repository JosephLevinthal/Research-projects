# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código
X = float(input("consumo:"))
Y = input("insira o tipo de instalacao: (R/I/C)").upper()
a = 0.44
b = 0.65
c = 0.55
d = 0.60
c1 =0.55
d1 = 0.60
print("Entradas:", X,"kWh e tipo",Y)

if((Y != "R") and (Y != "I") and (Y != "C") or (X < 0)):
	print("Dados invalidos")
	
elif(X <= 500 and Y == "R"):
	Z = X * a
	print("Valor total: R$", round(Z,2))
	
elif(X > 500 and Y == "R"):
	Z = X * b
	print("Valor total: R$", round(Z,2))
			
elif(X <= 1000 and Y == "C"):
	Z = X * c
	print("Valor total: R$", round(Z,2))
				
elif(X > 1000 and Y == "C"):
	Z = X * d
	print("Valor total: R$", round(Z,2))
		
elif(X <= 5000 and Y == "I"):
	Z = X * c1
	print("Valor total: R$", round(Z,2))
			
elif(X > 5000 and Y == "I"):
	Z = X * d1
	print("Valor total: R$",  round(Z,2))
