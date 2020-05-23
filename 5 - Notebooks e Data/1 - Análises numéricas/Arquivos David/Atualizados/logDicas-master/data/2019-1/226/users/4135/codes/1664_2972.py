so = int(input("Digite a posicao inicial do objeto:"))
v = int(input("Digite a velocidade do objeto:"))
t = int(input("Digite o tempo de deslocamento:"))
s = so+(v*t)
if (s>=1000):
	print(s)
	print("Sim")
else:
	print(s)
	print("Nao")