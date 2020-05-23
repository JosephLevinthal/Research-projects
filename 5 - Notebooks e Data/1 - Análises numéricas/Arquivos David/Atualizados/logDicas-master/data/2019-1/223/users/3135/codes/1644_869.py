# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
p=float(input("Insira o valor das compras:"))
desc= p * (5/100)
if (p>=200):
	pf= p- desc
else:
	pf= p
print(round(pf,2))