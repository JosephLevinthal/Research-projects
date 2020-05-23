a = input("E mulher?(S/N) ")
b = float(input("valor do ingresso: "))
c = int(input("Quantidade de ingressos comprados: "))

preco = b * c

if( "S" == a ):
	custo = b*c - (preco * 0.2)
else: 
	custo = b * c

print(round(custo, 2))
