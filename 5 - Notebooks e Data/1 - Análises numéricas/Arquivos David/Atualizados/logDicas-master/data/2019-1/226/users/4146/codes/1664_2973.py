s0 = int(input("Posicao inicial: "))
v = int(input("Velocidade: "))
t = int(input("Tempo: "))

s = s0 + v*t
print(s)

if (v <= 100):
	mensagem = "OK"
else:
	mensagem = "ACIMA"
	
print(mensagem)	