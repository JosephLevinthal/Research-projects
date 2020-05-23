# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("variavel a: "))
b = float(input("variavel b: "))
c = float(input("variavel c: "))
d = float(input("variavel d: "))

print("Intervalo 1: ",a,",",b)
print("Intervalo 2: ",c,",",d)

if not((b > a) and (d > c)):
	print("Entradas invalidas")
elif ((a < c) and (b > d)) or ((a > c) and (b < d)) or ((a == c) and (b == d)):
	print("Ha intersecao")
else:
	print("Nao ha intersecao")