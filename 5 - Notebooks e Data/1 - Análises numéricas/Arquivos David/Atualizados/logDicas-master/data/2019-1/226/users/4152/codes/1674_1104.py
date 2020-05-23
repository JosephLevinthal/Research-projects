# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("Digite aqui o valor de a: "))
b = float(input("Digite aqui o valor de b: "))
c = float(input("Digite aqui o valor de c: "))
d = float(input("Digite aqui o valor de d: "))
if ((b <= a) or (d <= c)):
	print("Intervalo 1:", a,",", b)
	print("Intervalo 2:", c,",", d)
	print("Entradas invalidas")
elif (b < c):
	print("Intervalo 1:", a,",", b)
	print("Intervalo 2:", c,",", d)
	print("Nao ha intersecao")
else:
	print("Intervalo 1:", a,",", b)
	print("Intervalo 2:", c,",", d)
	print("Ha intersecao")
