# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = input("Entrada: ")
print("Entrada:",a)
if a == "lobo" or a == "leao" or a == "veado" or a == "dragao" or a == "rosa" or a == "sol" or a == "lula" or a == "esfolado" or a == "turta":
	if a=="lobo":
		print("Casa: Stark")
	elif a =="leao":
		print("Casa: Lannister")
	elif a =="veado":
		print("Casa: Baratheon")
	elif a =="dragao":
		print("Casa: Targaryen")
	elif a =="rosa":
		print("Casa: Tyrell")
	elif a =="sol":
		print("Casa: Martell")
	elif a == "lula":
		print("Casa: Greyjoy")
	elif a == "esfolado":
		print("Casa: Bolton")
	elif a == "turta":
		print("Casa: Tully")
else:
	print("Brasao invalido")