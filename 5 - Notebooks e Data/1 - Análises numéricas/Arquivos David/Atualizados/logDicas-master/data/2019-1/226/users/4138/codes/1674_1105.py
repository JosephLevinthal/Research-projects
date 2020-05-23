# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
c = input("insira a descricao do brasao:").lower()
print("Entrada:", c)
if(c == "lobo"):
	print("Casa: Stark")

elif(c == "leao"):
	print("Casa: Lannister")
	
elif(c == "veado"):
	print("Casa: Baraethon")
	
elif(c == "dragao"):
	print("Casa: Targaryen")

elif(c == "rosa"):
	print("Casa: Tyrell")

elif(c == "sol"):
	print("Casa: Martell")
	
elif(c == "lula"):
	print("Casa: Greyjoy")

elif(c == "esfolado"):
	print("Casa: Bolton")

elif(c == "turta"):
	print("Casa: Tully")
else:
	print("Brasao invalido")
	