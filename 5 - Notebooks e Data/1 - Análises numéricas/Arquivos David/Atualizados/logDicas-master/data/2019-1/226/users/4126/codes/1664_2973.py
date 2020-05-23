S0 = int(input("posicao inicial:"))
v = int(input("velocidade final:"))
t = int(input("tempo de deslocamento:"))
S = S0 + v * t
print(S)
if(v <= 100):
	print("OK")
else:
	print("ACIMA")
