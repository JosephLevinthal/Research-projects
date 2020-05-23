

t = int(input("Digite o tempo em meses: "))

i = ((1042000/1500)**(1/t)) - 1

if( i <= 0.01 ):
	mensagem = "Real"
else:
	mensagem = "Irreal"

print(round(i,5))
print(mensagem)