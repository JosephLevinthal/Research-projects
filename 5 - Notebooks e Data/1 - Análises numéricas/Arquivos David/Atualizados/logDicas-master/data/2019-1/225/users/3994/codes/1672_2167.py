# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
n= input("Digite a cidade: ")
p= input("Digite o percurso: ")
if(n!="Belem" and n!="Borba" and n!="Coari" and n!="Humaita" and n!="Manicore" and n!="Maues"):
	mensagem="Destino inexistente"
	print(mensagem)
else:
	if(n=="Belem" and p=="ida"):
		mensagem="350.0"
		print(mensagem)
	elif(n=="Belem" and p=="ida-e-volta"):
		mensagem="650.0"
		print(mensagem)
	if(n=="Borba" and p=="ida"):
		mensagem="80.0"
		print(mensagem)
	elif(n=="Borba" and p=="ida-e-volta"):
		mensagem="152.0"
		print(mensagem)
	if(n=="Coari" and p=="ida"):
		mensagem="106.0"
		print(mensagem)
	elif(n=="Coari" and p=="ida-e-volta"):
		mensagem="199.0"
		print(mensagem)
	if(n=="Humaita" and p=="ida"):
		mensagem="200.0"
		print(mensagem)
	elif(n=="Humaita" and p=="ida-e-volta"):
		mensagem="390.0"
		print(mensagem)
	if(n=="Manicore" and p=="ida"):
		mensagem="150.0"
		print(mensagem)
	elif(n=="Manicore" and p=="ida-e-volta"):
		mensagem="280.0"
		print(mensagem)
	if(n=="Maues" and p=="ida"):
		mensagem="100.0"
		print(mensagem)
	elif(n=="Maues" and p=="ida-e-vinda"):
		mensagem="190.0"
		print(mensagem)

	
	