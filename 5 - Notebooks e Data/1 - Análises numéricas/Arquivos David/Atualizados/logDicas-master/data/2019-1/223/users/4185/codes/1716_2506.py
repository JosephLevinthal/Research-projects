anos= 0 
quantidade= float(input("digite a quantidade: "))
percentual_crescimento= float(input("digite o percentual: "))
qtd_retirada_ano= float(input("digite a retirada: "))

while  (0 < quantidade < 12000):
	acrescimo= quantidade * percentual_crescimento/100
	quantidade += acrescimo
	quantidade -= qtd_retirada_ano
	anos += 1 
	
   if (quantidade <= 0):
	print("EXTINCAO")
	
   else:
	PRINT("LIMITE")