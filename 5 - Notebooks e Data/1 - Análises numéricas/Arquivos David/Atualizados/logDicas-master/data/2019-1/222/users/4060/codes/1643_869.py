# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor=float(input("preco da compra: "))
if(valor>=200):
	men=valor-((5/100)*valor)
else:
	men=valor
print(round(men, 2))