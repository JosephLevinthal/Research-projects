# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
p = float(input("valor da compra: "))

if(p >= 200):
	pa = p - p*5/100
else:
	pa = p
print(round(pa,2))