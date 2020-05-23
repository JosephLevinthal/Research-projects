So=int(input("qual sua posicao inicial?"))
v=int(input("qual sua velocidade?"))
t=int(input("qual o seu tempo de deslocamento?"))
S=So+(v*t)
if (S>=1000):
	print(S)
	print('Sim')
else:
	print(S)
	print('Nao')