# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x=float(input(""))
if(x>=200):
	msg=x- ((5/100)*x)
else: 
	msg=x
print(round(msg, 2))
