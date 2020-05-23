gto= input("insira o Brasao: ").lower()
print("Entrada:",gto)
if (gto=="lobo") or (gto=="leao") or (gto=="veado") or (gto=="dragao") or (gto=="rosa") or (gto=="sol") or(gto=="lula") or(gto=="esfolado")or(gto=="turta"):
	if (gto=="lobo"):
		print("Casa: Stark")
	elif(gto=="leao"):
		print("Casa: Lannister")
	elif(gto=="veado"):
		print("Casa: Baratheon")
	elif(gto=="dragao"):
		print("Casa: Targaryen")
	elif(gto=="rosa"):
		print("Casa: Tyrell")
	elif(gto=="sol"):
		print("Casa: Martell")
	elif(gto=="lula"):
		print("Casa: Greyjoy")
	elif(gto=="esfolado"):
		print("Casa: Bolton")
	elif(gto=="turta"):
		print("Casa: Tully")
else:
	print("Brasao invalido")