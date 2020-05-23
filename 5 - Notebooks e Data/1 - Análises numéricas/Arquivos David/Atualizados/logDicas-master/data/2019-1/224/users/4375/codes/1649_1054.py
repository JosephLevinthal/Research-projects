# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("Digite ponto x: "))
y = float(input("Digite ponto y: "))
r = (2*x) + y == 3
if(r):
	mensagem = "ponto pertence a reta"
	print(mensagem.lower())
else:
	mensagem = "ponto nao pertence a reta"
	print(mensagem.lower())