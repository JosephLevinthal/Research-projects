s0=int(input("posicao inicial:"))
v=int(input("velocidade do objeto:" ))
t=int(input("tempo de deslocamento:"))
s=s0+(v*t)
print(s)
if(s<=t):
	print("sim")
else:
	print("nao")
	