# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

x = float(input("Valor de x: "))
y = float(input("Valor de y: "))

valor = 2 * x + y

if valor == 3:
	mensagem = "Ponto pertence a reta"
else:
	mensagem = "Ponto nao pertence a reta"
	
print (mensagem.lower())