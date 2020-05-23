so = int(input("Qual a posicao inicial? "))
v = int(input("Qual a velocidade do objeto? "))
t = int(input("Qual o tempo de deslocamento?" ))
s = so + ( v * t )

if(s >= 1000):
	print(s)
	print("Sim")
	
else:
	print(s)
	print("Nao")