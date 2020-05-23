# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco=float(input("preco:"))
if(preco>=200.00):
	valor=float(preco-(preco*5/100))
	
else:
	valor=(preco)
print(round(valor,2))