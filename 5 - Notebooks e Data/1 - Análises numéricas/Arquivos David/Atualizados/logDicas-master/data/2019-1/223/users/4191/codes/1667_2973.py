p=int(input("posicao inicial do objeto: "))
v=int(input("velocidade do objeto:  "))
t=int(input("tempo de deslocamento: "))
S=p+v*t
if (S<=100):
	mensagem = 'OK'
else:
	mensagem = 'ACIMA'
print(S)
print(mensagem)