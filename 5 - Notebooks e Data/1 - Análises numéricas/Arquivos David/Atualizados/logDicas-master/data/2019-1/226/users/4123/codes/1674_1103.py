# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input())
a = float(input())
b = float(input())
if a<=x<=b:
	print(x," pertence ao intervalo ",a,", ",b)
elif not(a<=x<=b) and b>a:
	print(x," nao pertence ao intervalo ",a,", ",b)
else:
	print("Entradas",a," e ",b," invalidas")
