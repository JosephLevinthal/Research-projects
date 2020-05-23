# Entrada
B = input("Brasao: ")
print("Entrada: ", B)
# Condicoes
if (B == "lobo"):
	print("Casa: Stark")
elif (B == "leao"):
	print("Casa: Lannister")
elif (B == "veado"):
	print("Casa: Baratheon")
elif (B == "dragao"):
	print("Casa: Targaryen")
elif (B == "rosa"):
	print("Casa: Tyrell")
elif (B == "sol"):
	print("Casa: Martell")
elif (B == "lula"):
	print("Casa: Greyjoy")
elif (B == "esfolado"):
	print("Casa: Bolton")
elif (B == "turta"):
	print("Casa: Tully")
elif (B != "lobo") or (B != "leao") or (B != "veado") or (B != "dragao") or (B != "rosa") or (B != "lula") or (B != "esfolado") or (B != "turta"):
	print("Brasao invalido")