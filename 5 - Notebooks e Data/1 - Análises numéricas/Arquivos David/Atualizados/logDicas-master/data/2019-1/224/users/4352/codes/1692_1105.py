brasao = input("digite seu brasao: ")
e = "Entrada: "
c = "Casa: "
i = "Brasao invalido"
print(e,brasao)
if brasao == "lobo":
	print(c + "Stark")
elif brasao == "leao":
	print(c + "Lannister")
elif brasao == "veado":
	print(c + "Baratheon")
elif brasao == "dragao":
	print(c + "Targaryen")
elif brasao == "rosa":
	print(c + "Tyrell")
elif brasao == "sol":
	print(c + "Martell")
elif brasao == "lula":
	print(c + "Greyjoy")
elif brasao == "esfolado":
	print(c + "Bolton")
elif brasao == "turta":
	print(c + "Tully")
else: 
	print(i)