# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor = float(input("Digite um numero: "))

if(valor >= 200):
	mensagem = valor-(valor*5/100)
else:
	mensagem = valor

print(round(mensagem, 2))
