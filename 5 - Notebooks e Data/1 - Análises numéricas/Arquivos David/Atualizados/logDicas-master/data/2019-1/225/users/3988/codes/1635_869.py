# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
var = float(input("valor:"))
if (var>=200):
	var = (var - (var * 0.05))
else:
	var = var
print(round(var, 2))	