# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
px = float(input("x de p: "))
py = float(input("y de p: "))

if(2*px + py == 3):
	mensagem = "ponto pertence a reta"
else:
	mensagem = "ponto nao pertence a reta"

print(mensagem)