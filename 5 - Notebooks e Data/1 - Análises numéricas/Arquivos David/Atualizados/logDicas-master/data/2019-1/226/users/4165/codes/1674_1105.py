brasao = input("digite o brasao:").lower()
print("Entrada: ",brasao)

if(brasao=="lobo"):
	x = "casa: Stark"
elif(brasao=="leao"):
	x = "Casa: Lannister"
elif(brasao=="veado"):
	x = "Casa: Baratheon"
elif(brasao=="dragao"):
	x = "Casa: Targaryen"
elif(brasao=="rosa"):
	x = "Casa: Tyrell"
elif(brasao=="sol"):
	x = "Casa: Martell"
elif(brasao=="lula"):
	x = "Casa: Greyjoy"
elif(brasao=="esfolado"):
	x = "Casa: Bolton"
elif(brasao=="turta"):
	x = "Casa: Tully"
else:
	x = "Brasao invalido"
print(x)
