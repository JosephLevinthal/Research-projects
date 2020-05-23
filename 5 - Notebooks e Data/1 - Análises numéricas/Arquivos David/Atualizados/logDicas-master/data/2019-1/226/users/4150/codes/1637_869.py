# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

compra = float(input("valor da compra: "))

desconto = compra * 0.05

if (compra >= 200) :
	valor = compra - desconto
else :
	valor = compra
print(round (valor, 2))
	