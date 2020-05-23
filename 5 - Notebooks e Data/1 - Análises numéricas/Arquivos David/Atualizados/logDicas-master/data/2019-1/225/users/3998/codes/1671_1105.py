# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
d = input("Brasao: ")
print("Entrada:", d)

if(d.lower() == "lobo"):
	print("Casa: Stark")
elif(d.lower() == "leao"):
	print("Casa: Lannister")
elif(d.lower() == "veado"):
	print("Casa: Baratheon")
elif(d.lower() == "dragao"):
	print("Casa: Targaryen")
elif(d.lower() == "rosa"):
	print("Casa: Tyrell")
elif(d.lower() == "sol"):
	print("Casa: Martell")
elif(d.lower() == "lula"):
	print("Casa: Greyjoy")
elif(d.lower() == "esfoldo"):
	print("Casa: Bolton")
elif(d.lower() == "turta"):
	print("Casa: Tully")
else:
	print("Brasao invalido")