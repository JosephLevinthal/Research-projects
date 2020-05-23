# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))
d = float(input("valor de d: "))
print("Intervalo 1: ", a,",", b)
print("Intervalo 2: ", c,",", d)
if (b<a) or (d<c):
	print("Entradas invalidas")
elif (c<=b) and (d>=a):
	print("Ha intersecao")
else:
	print("Nao ha intersecao")


	
	