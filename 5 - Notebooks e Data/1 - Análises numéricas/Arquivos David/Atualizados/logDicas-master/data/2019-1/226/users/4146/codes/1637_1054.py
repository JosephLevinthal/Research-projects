# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x0 = float(input("Digite o ponto x: "))
y0 = float(input("Digite o ponto y: "))

reta = 2*x0 + y0

if (reta == 3):
	mensagem = "ponto pertence a reta"
else:
	mensagem = "ponto nao pertence a reta"
	
print(mensagem)
