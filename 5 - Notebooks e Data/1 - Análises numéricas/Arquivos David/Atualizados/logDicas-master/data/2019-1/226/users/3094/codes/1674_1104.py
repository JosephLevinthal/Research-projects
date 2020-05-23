# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

a = float(input(""))
b = float(input(""))
c = float(input(""))
d = float(input(""))

print("Intervalo 1:", a, ",", b)
print("Intervalo 2:", c, ",", d)

if(b > a) and (d > c):
	if(c>=a and c<=b):
		print("Ha intersecao")
	else:
		print("Nao ha intersecao")
else:
	print("Entradas invalidas")