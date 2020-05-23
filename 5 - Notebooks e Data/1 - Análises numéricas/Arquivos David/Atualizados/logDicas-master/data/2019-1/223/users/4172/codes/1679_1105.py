# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
A=input("Brasao: ")

if (A=="lobo")or(A=="leao")or(A=="veado")or(A=="dragao")or(A=="rosa")or(A=="sol")or(A=="lula")or(A=="esfolado")or(A=="turta"):
	if(A=="lobo"):
		Y="Stark"
	elif(A=="leao"):
		Y="Lannister"
	elif(A=="veado"):
		Y="Baratheon"
	elif(A=="dragao"):
		Y="Targaryen"
	elif(A=="rosa"):
		Y="Tyrell"
	elif(A=="sol"):
		Y="Martell"
	elif(A=="lula"):
		Y="Greyjoy"
	elif(A=="esfolado"):	
		Y="Bolton"
	elif(A=="turta"):
		Y="Tully"
	print("Entrada:", A)
	print("Casa:", Y)
else:
	print("Entrada:", A)
	print("Brasao invalido")