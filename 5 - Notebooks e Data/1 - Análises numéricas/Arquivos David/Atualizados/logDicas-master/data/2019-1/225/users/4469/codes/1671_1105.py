# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x = input()

print("Entrada: " + x)

if(x.lower() == "lobo"):
	print("Casa: Stark")
elif(x.lower() == "leao"):
	print("Casa: Lannister")
elif(x.lower() == "veado"):
	print("Casa: Baratheon")
elif(x.lower() == "dragao"):
	print("Casa: Targaryen")
elif(x.lower() == "rosa"):
	print("Casa: Tyrell")
elif(x.lower() == "sol"):
	print("Casa: Martell")
elif(x.lower() == "lula"):
	print("Casa: Greyjoy")
elif(x.lower() == "esfolado"):
	print("Casa: Bolton")
elif(x.lower() == "turta"):
	print("Casa: Tully")
else:
	print("Brasao invalido")