# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
b = input("Digite o nome do brasao: ").lower()

if(b != "lobo" and b != "leao" and b != "veado" and b != "dragao" and b != "rosa" and b != "sol" and b != "lula" and b != "esfolado" and b != "turta"):
	print("Entrada:", b)
	print("Brasao invalido")
elif(b=="lobo"):
	print("Entrada:", b)
	print("Casa: Stark")
elif(b=="leao"):
	print("Entrada:", b)
	print("Casa: Lannister")
elif(b=="veado"):
	print("Entrada:", b)
	print("Casa: Baratheon")
elif(b=="dragao"):
	print("Entrada:", b)
	print("Casa: Targaryen")
elif(b=="rosa"):
	print("Entrada:", b)
	print("Casa: Tyrell")
elif(b=="lula"):
	print("Entrada:", b)
	print("Casa: Greyjoy")
elif(b=="esfolado"):
	print("Entrada:", b)
	print("Casa: Bolton")
elif(b=="turta"):
	print("Entrada:", b)
	print("Casa: Tully")
elif(b=="sol"):
	print("Entrada: ", b)
	print("Casa: Martell")

