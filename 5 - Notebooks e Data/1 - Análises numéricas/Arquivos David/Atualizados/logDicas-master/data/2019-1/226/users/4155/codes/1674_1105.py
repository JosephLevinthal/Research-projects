x = input("descricao do brasao: ")
print("Entrada:", x)

if ((x == "lobo") or (x == "leao") or (x == "veado") or (x == "dragao") or (x == "rosa") or (x == "sol") or (x == "lula") or (x == "esfolado") or (x == "turta")):

	if(x == "lobo"):
		print("Casa: Stark")
	elif(x == "leao"):
		print("Casa: Lannister")
	elif(x == "veado"):
		print("Casa: Baratheon")
	elif(x == "dragao"):
		print("Casa: Targaryen")
	elif(x == "rosa"):
		print("Casa: Tyrell")
	elif(x == "sol"):
		print("Casa: Martell")
	elif(x == "lula"):
		print("Casa: Greyjoy")
	elif(x == "esfolado"):
		print("Casa: Bolton")
	elif(x == "turta"):
		print("Casa: Tully")
else:
	print("Brasao invalido")