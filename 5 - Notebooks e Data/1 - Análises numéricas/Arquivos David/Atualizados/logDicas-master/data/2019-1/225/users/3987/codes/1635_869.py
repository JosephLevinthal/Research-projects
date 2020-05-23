# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("o preco e: "))
desconto = preco - (preco * (5/100))
if (preco > 200):
    print(round(desconto,2))
else:
	print("sem")