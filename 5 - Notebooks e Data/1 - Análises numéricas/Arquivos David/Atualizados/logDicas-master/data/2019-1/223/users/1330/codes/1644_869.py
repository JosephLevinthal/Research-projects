# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input())

if(x>=200.00):
	total = x -(x*0.05) 
else:
	total = x
print(round(total,2))