tambaqui = int(input("Quantidade inicial de Tambaquis: "))
ptamba = int(input("Percetual de crescimento dos tambaquis: "))
venda = int(input("Tambaquis retirados para venda: "))

ano = 0
ptamba = ptamba/100

while (tambaqui > 0 and tambaqui < 12000):
	tambaqui = tambaqui + (tambaqui*ptamba) 
	tambaqui = tambaqui - venda
	ano = ano + 1
	if(tambaqui > 12000):
		print("LIMITE")
	elif(tambaqui < 0):
		print("EXTINCAO")
		
print(ano)