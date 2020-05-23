# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor = float(input())

desconto = (valor*5) /100

pagar = valor - desconto

if(valor >= 200.00):
	mensagem = round(pagar,2)
else:
	 mensagem = round(valor,2)

print(mensagem)