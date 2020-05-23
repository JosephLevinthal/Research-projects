# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

a = float(input("digite o a: "))
b = float(input("digite o b: "))
c = float(input("digite o c: "))
d = float(input("digite o d: "))

print("Intervalo 1:" , a, "," ,b)
print("Intervalo 2:" , c, "," ,d)

if (b>a) and(d>c):
	if (c>=a) and (d<=b):
		print("Ha intersecao")
	else:
		print("Nao ha intersecao")
else:
	print("Entradas invalidas")
 