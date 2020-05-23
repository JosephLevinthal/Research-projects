brasao = input("Descricao do Brasao: ")

if (brasao == "lobo"):
	casa = "Stark"
elif (brasao == "leao"):
	casa = "Lannister"
elif (brasao == "veado"):
	casa = "Baratheon"
elif (brasao == "dragao"):
	casa = "Targaryen"
elif (brasao == "rosa"):
	casa = "Tyrell"
elif (brasao == "sol"):
	casa = "Martell"
elif (brasao == "lula"):
	casa = "Greyjoy"
elif (brasao == "esfolado"):
	casa = "Bolton"
elif (brasao == "turta"):
	casa = "Tully"
#else:
#	print ("Brasao invalido")

print ("Entrada: ", brasao)
if (brasao != "lobo" 
and brasao != "leao" 
and brasao != "veado" 
and brasao != "dragao" 
and brasao != "rosa" 
and brasao != "sol" 
and brasao != "lula" 
and brasao != "esfolado" 
and brasao != "turta"):
	print ("Brasao invalido")
else:
	print ("Casa: ", casa)