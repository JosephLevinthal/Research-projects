# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("Preco: "))

if(preco >= 200.00):
	valor_pago = preco - ((preco * 5) / 100)
else:
	valor_pago = preco

print(round(valor_pago, 2))	