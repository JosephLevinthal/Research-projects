var = float(input("valor consumido:"))
if(var<=300):
	mensagem = var*10/100
	total = mensagem + var
else:
	mensagem = var*6/100
	total = mensagem + var
print(round(total, 2))