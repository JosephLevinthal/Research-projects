# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a=float(input("valor da roupa sem desconto:"))
if(a>=200.0):
	v1= (5/100)* a
	v2= a - v1
else:
	v2= a
print(round(v2,2))
   