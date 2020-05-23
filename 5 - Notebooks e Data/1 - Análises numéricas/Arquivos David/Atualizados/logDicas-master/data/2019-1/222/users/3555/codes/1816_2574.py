i=0
mi=0
ma=0
senha = input() 
tamanho = int(len(senha))
if(tamanho >= 8 ):
	for i in tamanho:
		if(senha[i].islower()):
			mi = mi + 1
		else:
		   ma = ma + 1
	print(mi,ma)		
else:
		print("SENHA INVALIDA")
