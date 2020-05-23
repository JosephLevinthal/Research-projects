x1=int(input("posicao inicial:"))
v=int(input("velocidade do objeto:"))
t=int(input("tempo de deslocamento:"))
x2= x1 + (v*t)
if(x2 >= 1000):
	msg="Sim"
else:
	msg="Nao"
print(x2)
print(msg)