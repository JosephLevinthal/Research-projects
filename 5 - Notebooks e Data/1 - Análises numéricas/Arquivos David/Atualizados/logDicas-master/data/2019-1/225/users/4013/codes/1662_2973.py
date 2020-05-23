so = int(input("posicao inicial:"))
v = int(input("velocidade:"))
t = int(input("tempo:"))
s = so + (v * t)
if (v <= 100):
	msg = "OK"
else:
	msg = "ACIMA"
print(s)
print(msg)