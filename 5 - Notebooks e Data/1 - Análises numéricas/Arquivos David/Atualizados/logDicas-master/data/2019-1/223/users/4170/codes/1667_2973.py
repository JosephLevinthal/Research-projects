s0 = int(input("Posicao inicial: "))
v = int(input("Velocidade: "))
t = int(input("Tempo: "))
s = s0 + v * t
if(v<=100):
	print(s)
	print("OK")
else:
	print(s)
	print("ACIMA")