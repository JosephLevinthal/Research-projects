# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
e=input("Brasao:")
print("Entrada:", e)
if((e=="lobo")or(e=="leao")or(e=="veado")or(e=="dragao")or(e=="rosa")or(e=="sol")or(e=="lula")or(e=="esfolado")or(e=="turta")):
	if(e=="lobo"):
		msg="Stark"
		print("Casa:", msg)
	elif(e=="leao"):
		msg="Lannister"
		print("Casa:", msg)
	elif(e=="veado"):
		msg="Baratheon"
		print("Casa:", msg)
	elif(e=="dragao"):
		msg="Targaryen"
		print("Casa:", msg)
	elif(e=="rosa"):
		msg="Tyrell"
		print("Casa:", msg)
	elif(e=="sol"):
		msg="Martell"
		print("Casa:", msg)
	elif(e=="lula"):
		msg="Greyjoy"
		print("Casa:", msg)
	elif(e=="esfolado"):
		msg="Bolton"
		print("Casa:", msg)
	else:
		msg="Tully"
		print("Casa:", msg)
else:
	msg="Brasao invalido"
	print(msg)