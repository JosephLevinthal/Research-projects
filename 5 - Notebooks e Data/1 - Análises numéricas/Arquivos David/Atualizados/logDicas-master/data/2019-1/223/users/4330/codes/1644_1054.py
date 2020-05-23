# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a=float(input(""))
b=float(input(""))

p=2*a+b

if (p == 3):
	mensagem = "ponto pertence a reta"
else:
	mensagem = "ponto nao pertence a reta"
print(mensagem)