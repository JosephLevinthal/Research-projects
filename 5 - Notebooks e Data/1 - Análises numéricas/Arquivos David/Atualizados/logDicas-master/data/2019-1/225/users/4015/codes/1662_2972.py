ss=int(input("qual a posicao inicial do objeto?"))
v=int(input("qual a velocidade do objeto?"))
t=int(input("qual o tempo do objeto?"))
s=ss+v*t
if (s>=1000):
	print(s)
	print("Sim")
else:
	print(s)
	print("Nao")