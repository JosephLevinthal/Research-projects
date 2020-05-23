# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
price=float(input("price:"))
desc=((5/100)*price)
if(price>=200.0):
	print(round(price-desc, 2))
else:
	pint(price)