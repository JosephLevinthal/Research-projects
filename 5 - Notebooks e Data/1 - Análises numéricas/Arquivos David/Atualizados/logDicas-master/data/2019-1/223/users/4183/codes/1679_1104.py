# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("Ponto: "))
b = float(input("Ponto: "))
c = float(input("Ponto: "))
d = float(input("Ponto: "))
print("Intervalo 1: ", a, ",", b)
print("Intervalo 2: ", c, ",", d)

if (a > b or c > d):
	print("Entradas invalidas")
elif (b >= c or b >= d):
	print("Ha intersecao")
else:
	print("Nao ha intersecao")