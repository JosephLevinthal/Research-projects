# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

#Escreva uma progama que leia o brasão(Nomes):
nome_brasao=input("brasao: ")
# Como condição para o if e elif coloque todos os brasões, comparando-as sempre em letras minusculas ou maiusculas.
if (nome_brasao == "lobo") :
	print("Entrada: lobo")
	print("Casa: Stark")
elif (nome_brasao == "leao") :
	print("Entrada: leao")
	print("Casa: Lannister")
elif (nome_brasao == "veado") :
	print("Entrada: veado")
	print("Casa: Baratheon")
elif (nome_brasao == "dragao") :
	print("Entrada: dragao")
	print("Casa: Targaryen")
elif (nome_brasao == "rosa") :
	print("Entrada: rosa")
	print("Casa: Tyrell")
elif (nome_brasao == "sol") :
	print("Entrada: sol")
	print("Casa: Martell")
elif (nome_brasao == "lula") :
	print("Entrada: lula")
	print("Casa: Greyjoy")
elif (nome_brasao == "esfolado") :
	print("Entrada: esfolado")
	print("Casa: Bolton")
elif (nome_brasao == "turta") :
	print("Entrada: turta")
	print("Casa: Tully")
	
else :
	print("Entrada:", nome_brasao)
	print("Brasao invalido")
