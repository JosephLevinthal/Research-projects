# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco= float(input("qual o valor da compra? "))
if (preco>=200):
	msg= (preco-(preco*5/100))
else: 
	msg= (preco)
print(round(msg,2))