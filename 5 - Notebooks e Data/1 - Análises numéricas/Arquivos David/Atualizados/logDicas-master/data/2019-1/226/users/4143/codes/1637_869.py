# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a = float(input("Valor da roupa sem desconto:"))
if (a >= 200.0):
	eq = (5/100)* a
	eq2 = a - eq
else:
	eq2 = a
print(round(eq2,2))