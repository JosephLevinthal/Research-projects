# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

b = str(input("Digite seu brasao: "))

print("Entrada:", b)

if(b == "lobo"):
	print("Casa:", "Stark")
elif(b == "leao"):
	print("Casa:", "Lannister")
elif(b == "veado"):
	print("Casa:", "Baratheon")
elif(b == "dragao"):
	print("Casa:", "Targaryen")
elif(b == "rosa"):
	print("Casa:", "Tyrell")
elif(b == "sol"):
	print("Casa:", "Martell")
elif(b == "lula"):
	print("Casa:", "Greyjoy")
elif(b == "esfolado"):	
	print("Casa:", "Bolton")
elif(b == "turta"):
	print("Casa:", "Tully")
else:
	print("Brasao invalido")