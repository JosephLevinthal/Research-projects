# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("ponto x: "))
y = float(input("ponto y: "))
if 2*x+ y == 3:
	mensagem = "ponto pertence a reta"
else:
	mensagem = "ponto nao pertence a reta"
print(mensagem .lower())