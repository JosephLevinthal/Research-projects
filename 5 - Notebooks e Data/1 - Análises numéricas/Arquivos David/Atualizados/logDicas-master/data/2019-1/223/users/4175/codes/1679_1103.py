# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("x:"))
a = float(input("a:"))
b = float(input("b:"))
if (a <= x <= b):
	print(x,"pertence ao intervalo",  a,",",b)
elif x <= a <=b:
	print(x,"nao pertence ao intervalo", a,",",b)
elif b <= a:
	print("Entradas",  a,"e", b, " invalidas")
