# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

a = input("Brasao:")

print("Entrada:", a)

if (a == "lobo".lower()):
	print("Casa: Stark")
elif (a == "leao".lower()):
	print("Casa: Lannister")
elif (a == "veado".lower()):
	print("Casa: Baratheon")
elif (a == "dragao".lower()):
	print("Casa: Targaryen")
elif (a== "rosa".lower()):
	print("Casa: Tyrell")
elif (a == "sol".lower()):
	print("Casa: Martell")
elif (a == "lula".lower()):
	print("Casa: Greyjoy")
elif (a == "esfolado".lower()):
	print("Casa: Bolton")
elif (a == "turta".lower()):
	print("Casa: Tully")
else:
	print("Brasao invalido")