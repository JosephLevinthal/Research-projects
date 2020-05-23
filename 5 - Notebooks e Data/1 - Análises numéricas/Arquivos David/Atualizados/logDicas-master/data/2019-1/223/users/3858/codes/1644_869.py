# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
n = float(input())
if(n>=200):
	print(round(n-(n*0.05),2))
else:
	print(n)