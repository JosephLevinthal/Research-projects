so=int(input("posicao inicial do objeto:"))
v=int(input("velocidade do objeto:"))
t=int(input("tempo de deslocamento:"))
s=(so+(v*t))
print(s)
if(v>=100):
	mensagem="ACIMA"
else:
	mensagem="OK"
print(mensagem)
