# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x= float(input("Num x: "))
a= float(input("Num a: "))
b= float(input("Num b: "))
if(b>a):
	if(a<= x <=b):
		print(x, "pertence ao intervalo", a,",", b)
	elif((x<a) or (x>b)):
		print(x, "nao pertence ao intervalo", a, ",", b)
else: 
	print("Entradas", a, "e", b, "invalidas")