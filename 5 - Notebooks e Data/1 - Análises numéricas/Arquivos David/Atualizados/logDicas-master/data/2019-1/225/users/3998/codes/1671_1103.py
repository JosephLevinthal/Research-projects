# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("x: "))
a = float(input("a: "))
b = float(input("b: "))

if(b<=a):
	print("Entradas",a, "e" ,b, "invalidas")
elif(a<=x) and (x<=b):
	print(x,"pertence ao intervalo",a,",",b)
else:
	print(x,"nao pertence ao intervalo",a,",",b)