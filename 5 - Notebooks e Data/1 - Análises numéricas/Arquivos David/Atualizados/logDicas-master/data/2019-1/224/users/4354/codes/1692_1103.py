# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("numero real x: "))
a = float(input("numero real a: "))
b = float(input("numero real b: "))
if(a<= x <= b):
	print(x,"pertence ao intervalo", a,",",b)
elif(b<=a):
	print("Entradas",a,"e",b,"invalidas")
elif(x<a or x>b):
	print(x,"nao pertence ao intervalo", a,",",b)

else:
	print("Entradas",a,"e",b,"invalidas")
	
