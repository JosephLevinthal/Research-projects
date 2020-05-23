# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código
x= float(input("Valor da compra?"))

if (x >= 200):
	k= (x-(x*5/100))
else:
	k= x
print(round(k, 2))