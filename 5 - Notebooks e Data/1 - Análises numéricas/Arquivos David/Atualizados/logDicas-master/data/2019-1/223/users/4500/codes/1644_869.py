# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
desconto = float(input("x: "))

if (desconto % 5 >=200):
	x = "conceder desconto"
	
else:
	x = "nao conceder desconto"
	
print (x)