peixes = int(input("Quantidade inicial de tambaquis no tanque: "))
percent = float(input("Percentual de crescimento anual da quantidade de tambaquis: "))
venda = int(input("Quantidade de tambaquis retirados todos os anos para venda: "))

anos = 0
cap = 12000

while(peixes < cap and peixes > 0):
	peixes = peixes - venda + (peixes * percent / 100)
	anos = anos + 1
	
if(peixes <= 0):
	print("EXTINCAO")
elif(peixes >= cap):
	print("LIMITE")
	
print(anos)