# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x = input("insira a resposta da questao 1:")
y = input("insira a resposta da questao 2:")
z = input("insira a resposta da questao 3:")
i = input("insira o gabarito da questao 1:")
j = input("insira a gabarito da questao 2:")
k = input("insira o gabarito da questao 3:")
# e,d,c
if(x != i and y != j and z != k):
	print(0)
elif(x == i and y != j and z != k):
	print(1)
elif(x != i and y == j and z != k):
	print(1)
elif(x != i and y != j and z == k):
	print(1)
elif(x == i and y == j and z != k):
	print(2)
elif(x == i and y != j and z == k):
	print(2)
elif(x != i and y == j and z != k):
	print(2)
else:
	print(3)


	