# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = int(input("Digite aqui a coordenada x: "))

y = int(input("Digite aqui a coordenada y: "))

if (2 * x + y == 3):
	resultado = "ponto pertence a reta"
else:
	resultado = "ponto nao pertence a reta"
	
print(resultado)