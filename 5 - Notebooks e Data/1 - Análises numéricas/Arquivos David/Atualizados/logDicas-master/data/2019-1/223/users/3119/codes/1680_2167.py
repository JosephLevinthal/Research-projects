# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

destino = input("Nome da cidade de destino: ")
percuso = input("ida ou ida-e-volta? ")

if(destino == "Belem" and percuso == "ida"):
	print("350.0")
elif(destino == "Belem" and percuso == "ida-e-volta"):
	print("650.0")
elif(destino == "Borba" and percuso == "ida"):
	print("80.0")
elif(destino == "Borba" and percuso == "ida-e-volta"):
	print("152.0")
elif(destino == "Coari" and percuso == "ida"):
	print("106.0")
elif(destino == "Coari" and percuso == "ida-e-volta"):
	print("199.0")
elif(destino == "Humaita" and percuso == "ida"):
	print("200.0")
elif(destino == "Humaita" and percuso == "ida-e-volta"):
	print("390.0")
elif(destino == "Manicore" and percuso == "ida"):
	print("150.0")
elif(destino == "Manicore" and percuso == "ida-e-volta"):
	print("280.0")
elif(destino == "Maues" and percuso == "ida"):
	print("100.0")
elif(destino == "Maues" and percuso == "ida-e-volta"):
	print("190.0")
else:
	print("Destino inexistente")