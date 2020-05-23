# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu códx
x=float(input("x:   "))
a=float(input("a:   "))
b=float(input("b:   "))
if(b>a):
	if(x<=b)and(x>=a):
		print(x,"pertence ao intervalo ",a,", ",b)
	else:
		print(x,"nao pertence ao intervalo ",a,", ",b)
else:
	print("Entradas ",a," e ",b," invalidas")