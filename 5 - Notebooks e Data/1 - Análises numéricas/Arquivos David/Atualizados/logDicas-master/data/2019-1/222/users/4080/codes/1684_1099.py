# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x = float(input("entrada a; "))
y = float(input("entrada b; "))
z = float(input("entrada c; "))
print("Entradas:", x, ",", y, ",", z)
#arrumar as ordes apartir daqui
if ((x < y + z) and (y < x + z) and (z < y + x)):
	if ((x != y) and (y != z) and (z != x)):
		print("escaleno")
	else:
		if ((x != y) or (y != z)):
			print("isosceles")
		else:
			print("equilatero")
else:
	print("Tipo de triangulo: invalido")

