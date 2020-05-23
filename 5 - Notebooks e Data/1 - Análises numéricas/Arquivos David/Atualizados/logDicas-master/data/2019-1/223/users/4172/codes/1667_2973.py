S1=int(input("posicao inicial: "))
V=int(input("velocidade do objeto: "))
T=int(input("tempo de deslocamento: "))

S = S1 + (V*T)

ML=100
if V <= ML:
	mensagem = S
	mensagem1 ='OK'
else:
	mensagem = S
	mensagem1 = 'ACIMA'
	
print(mensagem)
print(mensagem1)