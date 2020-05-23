# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
p = float(input("Preco: "))
if (p >= 200):
	valor = p - (p * (5/100))
else: 
	valor = p
print(round(valor, 2))