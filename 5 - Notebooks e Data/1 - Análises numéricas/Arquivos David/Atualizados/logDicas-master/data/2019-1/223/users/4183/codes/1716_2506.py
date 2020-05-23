anos = 0
tem = int(input("Digite a quantidade inicial de tambaquis do tanque de Ariene: "))
cresce = float(input("Digite o percentual de crescimento anual do quantidade de tambaquis: "))
tira = int(input("Digite a quantidade de tambaquis retirados para venda: "))
while ( tem > 0 and tem < 12000): 
	
	tem = tem + (tem*cresce)/100
	tem = tem - tira 
	anos = anos + 1
if (tem <= 0):
	print("EXTINCAO")
else:
	print("LIMITE")
print(anos)
	

