# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("ponto a: "))
b = float(input("ponto b: "))
c = float(input("ponto c: "))
d = float(input("ponto d: "))
print("Intervalo 1:",a,",",b)
print("Intervalo 2:",c,",",d)
if b > a and d > c:
	if (a <= d <=b) or (a<= c <= b):
		print("Ha intersecao")
	else:
		print("Nao ha intersecao")
else:
	print("Entradas invalidas")
