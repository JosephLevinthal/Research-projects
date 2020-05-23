# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
#Descont de 5% para 200 ou mais

preco = float(input("Valor sem desconto: "))

eq = preco - ((5/100) * preco)

if (preco >= 200.00):
	msg = eq
else:
	msg = preco
print(round(msg, 2))