# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x = input("nome da casa: ")
print("Entrada:", x)
if (x == "lobo" or "leao" or "veado" or "dragao" or "rosa" or "sol" or "lula" or "esfolado" or "turta"	):
	if (x == "lobo"):
		mensagem = "Stark"
		print("Casa:" , mensagem)
	elif (x == "leao"):
		mensagem = "Lannister"
		print("Casa:" , mensagem)
	elif (x == "veado"):
		mensagem = "Baratheon"
		print("Casa:" , mensagem)
	elif (x == "dragao"):
		mensagem = "Targaryen"
		print("Casa:" , mensagem)
	elif (x == "rosa"):
		mensagem = "Tyrell"
		print("Casa:" , mensagem)
	elif (x == "sol"):
		mensagem = "Martell"
		print("Casa:" , mensagem)
	elif (x == "lula"):
		mensagem = "Greyjoy"
		print("Casa: Greyjoy")
	elif (x == "esfolado"):
		mensagem = "Bolton"
		print("Casa:" , mensagem)
	elif (x == "turta"):
		mensagem = "Tully"
		print("casa: Tully")
	else:
		print("Brasao invalido")
else:
	print("Brasao invalido")
