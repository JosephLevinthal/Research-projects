jogo = int(input("Numero apostado pelo jogador: "))
loteria = int(input("Numero sorteado na loteria: "))

j = (jogo // 10) % 10
j1 = jogo % 10
l = (loteria // 10) % 10
l1 = loteria % 10

if(jogo == loteria):
	print("Ganhou R$ 100.000,00")
elif(j1 == l and j == l1):
	print("Ganhou R$ 50.000,00")
elif(j == l1 or j == l or j1 == l1 or j1 == l):
	print("Ganhou R$ 1.000,00")
else:
	print("Perdeu")
	