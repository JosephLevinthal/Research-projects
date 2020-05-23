x = int(input("Posicao inicial:"))
v = int(input("Velocidade do objeto:"))
s = int(input("Tempo de deslocamento:"))

S = x + v*s

if(v<=100):
	msg = "OK"
else:
	msg = "ACIMA"

print(S)
print(msg)