S0 = int(input("Digite aqui a posicao inicial do objeto: "))
v = int(input("Digite aqui a velocidade do objeto: "))
t = int(input("Digite aqui o tempo de deslocamento: "))
S = S0 + v * t
print(S)
if(S < 1000):
	print("Nao")
else:
	print("Sim")
