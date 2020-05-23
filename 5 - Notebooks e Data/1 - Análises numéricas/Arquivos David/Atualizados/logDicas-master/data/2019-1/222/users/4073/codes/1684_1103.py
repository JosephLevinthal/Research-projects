# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("x: "))
a = float(input("a: "))
b = float(input("b: "))
					 
if (b <= a):
	print("Entradas {} e {} invalidas".format(a,b))
					 
elif (a <= x and x <= b):
	print("{} pertence ao intervalo {} , {}".format(x,a,b))

else:
	print("{} nao pertence ao intervalo {} , {}".format(x,a,b))