# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

compras = float(input("valor das compras: "))
desconto = compras*0.05
if(compras>=200):
	valor = round(compras-desconto, 2)
else:
	valor = round(compras, 2)
print(valor)