# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("digite o valor da compra: "))
desc = preco - (preco * (5 / 100))
if (preco >= 200.00):
	men = round(desc,2)
else:
	men = round(preco,2)
print(men)