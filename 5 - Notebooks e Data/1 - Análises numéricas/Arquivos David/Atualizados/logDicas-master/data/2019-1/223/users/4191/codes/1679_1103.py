# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
X=float(input("Valor de x: "))
A=float(input("Valor de a: "))
B=float(input("Valor de b: "))
if((A<=X)and(B>=X)):
	print(X, "pertence ao intervalo", A, ",", B)
elif(B<=A):
	print('Entradas', A, 'e', B, 'invalidas')
elif((A>X)or(B<=X)):
	print(X, 'nao pertence ao intervalo', A, ',', B)