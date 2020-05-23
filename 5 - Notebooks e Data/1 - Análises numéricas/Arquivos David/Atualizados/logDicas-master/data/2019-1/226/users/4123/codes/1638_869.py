# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
prc = float(input())

if prc<200:
	print(round(prc,2))
else:
	print(round(prc-prc*0.05,2))
