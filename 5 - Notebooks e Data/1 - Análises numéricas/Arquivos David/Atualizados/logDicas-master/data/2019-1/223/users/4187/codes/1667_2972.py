s0 = int(input("posicao inicial do objeto:"))
v = int(input("velocidade do objeto:"))
t = int(input("tempo do deslocamento:"))

s= s0 + (v * t)
print(s)
sp = 1000
if(s >= sp):
	print('Sim')
	
else:
	print('Nao')