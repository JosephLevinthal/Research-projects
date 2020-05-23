x = (input("animal: ").lower())
print("Entrada:",x)
if((x=="lobo")or(x=="leao")or(x=="veado")or(x=="dragao")or(x=="rosa")or(x=="sol")or(x=="lula")or(x=="esfolado")or(x=="turta")):
	if(x=="lobo"):
		y = "Stark"
	elif(x=="leao"):
		y = "Lannister"
	elif(x=="veado"):
		y = "Baratheon"
	elif(x=="dragao"):
		y = "Targaryen"
	elif(x=="rosa"):
		y = "Tyrell"
	elif(x=="sol"):
		y = "Martell"
	elif(x=="lula"):
		y = "Greyjoy"
	elif(x=="esfolado"):
		y = "Bolton"
	elif(x=="turta"):
		y = "Tully"
	print("Casa: "+y)
else:
	print("Brasao invalido")