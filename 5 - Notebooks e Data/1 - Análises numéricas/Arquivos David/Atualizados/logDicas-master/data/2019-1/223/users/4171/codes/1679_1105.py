# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

brasao = input("descricao do brasao: ")

if brasao == "lobo" or brasao == "leao" or brasao == "veado" or brasao == "dragao" or brasao == "rosa" or brasao == "sol" or brasao == "lula" or brasao == "esfolado" or brasao == "turta":
	if brasao == "lobo":
		casa = ("Stark")
	elif brasao == "leao":
		casa = ("Lannister")
	elif brasao == "veado":
		casa = ("Baratheon")
	elif brasao == "dragao":
		casa = ("Targaryen")
	elif brasao == "rosa":
		casa = ("Tyrell")
	elif brasao == "sol":
		casa = ("Martell")
	elif brasao == "lula":
		casa = ("Greyjoy")
	elif brasao == "esfolado":
		casa = ("Bolton")
	elif brasao == "turta":
		casa = ("Tully")
	print("Entrada:", brasao)
	print("Casa:", casa)
else:
	print("Entrada: ", brasao)
	print("Brasao invalido")