# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x=float(input("numero real x: "))
a=float(input("numero real a: "))
b=float(input("numero real b: "))
if(b>a):
	if (a<x and x<b):
		print(x,"pertence ao intervalo",a,",",b)
	elif((x<a and a<b) or (a<b and b<x)):
		print(x,"nao pertence ao intervalo",a,",",b)
elif(b<=a):
	print("Entradas",a,"e",b,"invalidas")