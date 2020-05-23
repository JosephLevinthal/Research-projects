so=int(input("posicao inicial:"))
v=int(input("velocidade:"))
t=int(input("tempo de deslocamento:"))

s=so+(v*t)

if(s>=1000):
	a = ("Sim")
else:
	a = ("Nao")
print(s)
print(a)