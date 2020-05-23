n=input("nome da arma: ").upper()
d=int(input("destreza: "))
s1=int(input("valor sorteado1: "))
s2=int(input("valor sorteado2: "))
S=s1+s2
if((s1>=1 and s1<=10) and (s2>=1 and s2<=10) and (d>0)):
	if(S>=2 or S<=20):
		if(n=="CIMITARRA"):
			dano = (2*S)+(2*d)
			print(dano)
		elif(n=="KATANA"):
			dano=(2*S)+d
			print(dano)
		elif(n=="SABRE"):
			dano= S +2*d
			print(dano)
		else:
			print("Entrada invalida")
	else:
		print("Entrada invalida")
else:
	print("Entrada invalida")
	
			
			