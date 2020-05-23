anos = 0
quantidade = float(input("quantidade inicial de tambaquis: "))
percent = float(input("percentual de crescimento no tanque: "))
quant_retirada = float(input("quantidade retirada para a venda: "))
while(0 <quantidade < 12000):
	acrescimo = quantidade * percent/100
	quantidade += acrescimo
	quantidade -= quant_retirada
	anos += 1
if(quantidade <= 0):
	print("EXTINCAO")
else:
	print("LIMITE")
print(anos)
	