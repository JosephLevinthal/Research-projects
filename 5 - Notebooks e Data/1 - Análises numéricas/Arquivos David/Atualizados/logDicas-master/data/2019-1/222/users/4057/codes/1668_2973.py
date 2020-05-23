S0 = int(input("A posicao inicial em metros: "))
v = int(input("velocidade do objeto m/s "))
t = int(input("tempo de deslocamento: "))

S = S0 + (v * t)
if v <= 100 :
	print(S)
	print("OK")
else: 
	print(S)
	print("ACIMA")