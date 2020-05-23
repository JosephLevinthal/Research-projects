# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
casa=input("brasao:")
print("Entrada:",casa)
if (casa=="lobo")or(casa=="leao")or(casa=="veado")or(casa=="dragao")or(casa=="rosa")or(casa=="sol")or(casa=="lula")or(casa=="esfolado")or(casa=="turta"):
	if (casa=="lobo"):
		print("Casa: Stark")
	elif (casa=="leao"):
		print("Casa: Lannister")
	elif (casa=="veado"):
		print("Casa: Baratheon")
	elif (casa=="dragao"):
		print("Casa: Targaryen")
	elif (casa=="rosa"):
		print("Casa: Tyrell")
	elif (casa=="sol"):
		print("Casa: Maetell")
	elif (casa=="lula"):
		print("Casa: Greyjoy")
	elif (casa=="esfolado"):
		print("Casa: Bolton")
	elif (casa=="turta"):
		print("Casa: Tully")
else:
	print("Brasao invalido")