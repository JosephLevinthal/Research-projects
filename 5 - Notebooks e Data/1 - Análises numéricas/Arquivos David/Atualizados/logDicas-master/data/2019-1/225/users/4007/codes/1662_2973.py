S0 = int(input("posicao inicial(m):"))
v = int(input("velocidade(m/s): "))
t = int(input("tempo(s): "))
S = S0 + (v*t)

if (v <= 100):
	msg = "ok"
	
else:
	msg = "acima"
	
print(S)
print(msg.upper())
	
