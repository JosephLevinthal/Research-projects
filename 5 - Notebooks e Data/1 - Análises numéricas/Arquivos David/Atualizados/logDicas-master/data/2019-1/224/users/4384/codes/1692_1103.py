# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x=float(input("valor_de_x:" ))
a=float(input("valor_de_a:" ))
b=float(input("valor_de_b:" ))
if(a<x)and(b>x):
	print(x ,"pertence ao intervalo", a,",", b)
elif(b<a)or(a==b):
	print("Entradas", a ,"e", b ,"invalidas")
else:
	print(x ,"nao pertence ao intervalo", a,",", b)