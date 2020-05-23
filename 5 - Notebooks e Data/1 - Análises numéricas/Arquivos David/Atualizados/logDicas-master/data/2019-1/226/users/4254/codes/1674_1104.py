# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))

if(a>=b or c>=d):
	print("Intervalo 1:",a,",",b)
	print("Intervalo 2:",c,",",d)
	print("Entradas invalidas")
elif(b>=c and d>a or d>=a and b>c):
	print("Intervalo 1:",a,",",b)
	print("Intervalo 2:",c,",",d)
	print("Ha intersecao")
else:
	print("Intervalo 1:",a,",",b)
	print("Intervalo 2:",c,",",d)
	print("Nao ha intersecao")

