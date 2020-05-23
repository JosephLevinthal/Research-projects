a=input("nome da arma: ")
b=int(input("destreza: "))
c=int(input("valores sorteados: "))
d=int(input("dano: "))
if(c>2 and c>20):
	if(a.upper()=="CIMITARRA"):
		d=2*c+2*b
		print(d)
	elif(a.upper()=="KATANA"):
		d=2*c+b
		print(d)
	elif(a.upper()=="SABRE"):
		d=c+2*b
		print(d)
else:
	print("Entrada invalida")