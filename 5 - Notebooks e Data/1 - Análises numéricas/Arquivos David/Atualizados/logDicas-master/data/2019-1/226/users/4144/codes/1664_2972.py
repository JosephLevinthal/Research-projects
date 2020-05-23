s0 = int(input("posicao inicial do objeto: "))
vel = int(input("velocidade do objeto: "))
tempo = int(input("tempo: "))
S = s0 + (vel * tempo)
print(S)
if (S > 1000):
	print("Sim")
if (S < 1000):
	print("Nao")
