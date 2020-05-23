# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
coordenadax = float(input("x: "))
coordenaday = float(input("y: "))

if(2*coordenadax + coordenaday == 3):
	mensagem = "ponto pertence a reta"
	print(mensagem)
else:
	mensagem = "ponto nao pertence a reta"
	print(mensagem)