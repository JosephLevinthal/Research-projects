# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x=float(input("valor a ser pago:"))
if(x>=200):
	x=(x-(x*0.05))
else:
	x=x
print(round(x, 2))