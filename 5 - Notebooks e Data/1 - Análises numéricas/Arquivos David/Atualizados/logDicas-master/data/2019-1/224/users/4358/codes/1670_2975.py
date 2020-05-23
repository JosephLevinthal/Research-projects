qdsuc=int(input("quantidade de suco:"))
qdsal=int(input( "quantidade de salgado:"))
disponivel=float(input("Digite o valor disponivel:"))
suco=3
salgado=3.5
total=(qdsuc*suco)+(qdsal*salgado)
print(round(total,2))
if(disponivel>total):
	print("Sim")
else:
	print("Nao")