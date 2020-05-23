# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("escreva o nr real x: "))
a = float(input("escreva o nr real a: "))
b = float(input("escreva o nr real b: "))
if (b <= a):
	print ("Entradas", a,"e", b, "invalidas")
elif ((x >= a) and (x <= b) and (b > a)):
	print(x, "pertence ao intervalo",a,",",b)
else:
	print (x, "nao pertence ao intervalo",a,",",b)
