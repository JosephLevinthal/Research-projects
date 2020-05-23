# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("digite coordena x:"))
y = float(input("digite coordena y:"))
reta = 2*x+y 
if reta == 3:
	mensagem = "ponto pertence a reta"
else:
	mensagem = "ponto nao pertence a reta"
print(mensagem.lower())
