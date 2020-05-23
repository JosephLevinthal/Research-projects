# Teste seu código aos poucos.
comp = float(input( "preco")) 
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
if (comp>=200):
	x = comp-(comp * 0.05)
else: 
	x = comp
	
print(round(x, 2))