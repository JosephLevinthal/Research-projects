# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
b = input(" Digite o brasao: ")
print(" Entrada:",b)
if(b=="lobo" or b=="leao" or b=="veado" or b=="dragao" or b=="rosa" or b=="sol" or b=="lula" or b=="esfolado" or b=="turta"):
	if(b=="lobo"):
		mensagem = "Stark"
		print("Casa:",mensagem)
	elif(b=="leao"):
		mensagem = "Lannister"
		print("Casa:",mensagem)
	elif(b=="veado"):
		mensagem = "Baratheon"
		print("Casa:",mensagem)
	elif(b=="dragao"):
		mensagem = "Targaryen"
		print("Casa:",mensagem)
	elif(b=="rosa"):
		mensagem="Tyrell"
		print("Casa:",mensagem)
	elif(b=="sol"):
		mensagem= "Martell"
		print("Casa:",mensagem)
	elif(b=="lula"):
		mensagem="Greyjoy"
		print("Casa:",mensagem)
	elif(b=="esfolado"):
		mensagem="Bolton"
		print("Casa:",mensagem)
	else:
		mensagem= "Tully"
		print("Casa:",mensagem)
else:
	print(" Brasao invalido")
		