# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
destino = input("digite cidade: ")
percurso = input("digite percurso: ")

if(destino == "Belem"):
	if (percurso == "ida"):
		print("350.00")
	elif(percurso == "ida-e-volta"):
		print("650.00")
elif(destino == "Borba"):
	if (percurso == "ida"):
		print("80.00")
	elif(percurso == "ida-e-volta"):
		print("152.00")
elif(destino == "Coari"):
	if (percurso == "ida"):
		print("106.00")
	elif(percurso == "ida-e-volta"):
		print("199.00")
elif(destino == "Humaita"):
	if (percurso == "ida"):
		print("200.00")
	elif(percurso == "ida-e-volta"):
		print("390.00")
elif(destino == "Manicore"):
	if (percurso == "ida"):
		print("150.00")
	elif(percurso == "ida-e-volta"):
		print("280.00")
elif(destino == "Maues"):
	if (percurso == "ida"):
		print("100.00")
	elif(percurso == "ida-e-volta"):
		print("190.00")
else:
	print("Destino inexistente")
				
				