# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor = float(input("Digite o valor da compra:"))
if (valor >= 200):
	mensagem = valor*0.95
else:
	mensagem = valor
print (round (mensagem,2))


