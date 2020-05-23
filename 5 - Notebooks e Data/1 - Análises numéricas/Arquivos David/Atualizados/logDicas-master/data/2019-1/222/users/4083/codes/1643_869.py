# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
compras = float(input("Digite o valor da compra:"))
valor = compras*(95/100)

if  (compras >= 200):
    print(round(valor, 2))
	
else:
	 print(compras)