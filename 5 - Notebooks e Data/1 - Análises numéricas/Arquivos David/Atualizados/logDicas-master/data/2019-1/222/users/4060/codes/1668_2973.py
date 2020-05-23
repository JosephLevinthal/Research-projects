si=int(input("posicao inicial: "))
v=int(input("velocidade do objeto: "))
t=int(input("tempo de deslocamento: "))
sf=si+(v*t)
if(v<=100):
	print(sf)
	print("OK")
else:
	print(sf)
	print("ACIMA")