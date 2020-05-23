# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
p = float(input("preco da compra: "))

if (p >= 200):
	valor = p - ((5/100)*p)
else:
	valor = p
print(round(valor,2))