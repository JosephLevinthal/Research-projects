# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

num = int(input("Numero: "))
n1 = num%2
if (n1==0):
	mensagem = "PAR"
else:
	mensagem = "IMPAR"
print(mensagem.lower())