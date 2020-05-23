# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("valor de A: "))
b = float(input("valor de B: "))
c = float(input("valor de C: "))
d = float(input("valor de D: "))

print("Intervalo 1: ",a,",",b)
print("Intervalo 2: ",c,",",d)

if (b<=a) or (d<=c):
	print("Entradas invalidas")
elif (b<c):
	print("Nao ha intersecao")
else:
	print("Ha intersecao")