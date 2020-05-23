# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
#Intervalo 1
a = float(input("numero: "))
b = float(input("numero: "))
h = "Intervalo 1: "

#Intervalo 2
c = float(input("numero: "))
d = float(input("numero: "))
x = "Intervalo 2: "

if (b > a and d > c):
	if ((a<=c and b>=c) or b>=d and b>c and a<=c and a<=d):
		print(h,a,",",b)
		print(x,c,",",d)
		print("Ha intersecao")
	else:
		print(h,a,",",b)
		print(x,c,",",d)
		print("Nao ha intersecao")
else:
	print(h,a,",",b)
	print(x,c,",",d)
	print("Entradas invalidas")
	
		
		
		
		