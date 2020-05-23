numeroJogador = int(input("Numero apostado pelo jogador (com dois digitos):"))
numeroSorteado = int(input("Numero sorteado na loteria (tambem com dois digitos):"))

#isolamento dos digitos do numero do jogador
n1nj = (numeroJogador // 10 )
n2nj = (numeroJogador % 10)
#isolamento dos digitos do nunero sorteado
n1ns = (numeroSorteado // 10)
n2ns = (numeroSorteado % 10)

if(numeroJogador == numeroSorteado ):
	print("Ganhou R$ 100.000,00")
elif(n1nj == n2ns and n2nj == n1ns  ):
	print("Ganhou R$ 50.000,00")
elif(n1nj == n2ns or n2nj == n1ns or n1nj == n1ns or n2nj == n2ns ):
	print("Ganhou R$ 1.000,00")
else:
	print("Perdeu")