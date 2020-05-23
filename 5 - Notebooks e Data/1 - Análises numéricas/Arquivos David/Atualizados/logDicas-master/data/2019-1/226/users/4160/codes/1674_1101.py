# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
c = float(input("consumo: "))
t = input("Tipo de instalacao (R para residencias, I para industrias, C para comercios): ").upper()
h = "Valor total: R$ "
print("Entradas: ", c , "kWh" ,"e" ,"tipo " , t )

if(t=="R" and c>=0):
	if(c<= 500):
		x = c * 0.44 
		print(h,round(x,2))
	else:
		x = c * 0.65 
		print(h, round(x,2)) 
elif(t=="C" and c>=0):
	if(c<=1000):
		x = c * 0.55 
		print(h,round(x,2))
	else:
		x = c * 0.60 
elif(t=="I" and c>=0):
	if(c<= 5000):
		x = c * 0.55 
		print(h, round(x,2))
	else:
		x = c * 0.6 
		print(h,round(x,2))
if(c<0):
	print("Dados invalidos")


