valor=float(input("valor: "))
ru=float(input("ru: "))
tickets=float(input("tickets: "))
passes=float(input("passes: "))
valordospasses=float(input("valor dos passes"))
a = float(ru*tickets+passes*valordospasses)
					 
if (valor>=a):
	mensagem = "SUFICIENTE"
	print(mensagem)
				  
else:
	mensagem = "INSUFICIENTE"
	print(mensagem)
					 
