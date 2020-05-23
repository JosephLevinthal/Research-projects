# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor=float(input("compra:"))
valor_minimo=200
if(valor>=200):
	compra=valor-(valor*5/100)
else:
	compra=valor
print(round(compra,2))	