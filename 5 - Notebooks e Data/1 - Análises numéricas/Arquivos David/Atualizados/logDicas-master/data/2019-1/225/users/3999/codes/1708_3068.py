x=input().upper()
D=int(input("destreza:"))
d1=int(input("valor sorteado1:"))
d2=int(input("valor sorteado2: "))
S= d1+d2
if((x!="CIMITARRA")or(x!="KATNA")or(x!="SABRE")or(d1<1)or(d2<1)or(d1>10)or(d2>10)or(D<0)):
	print("Entrada invalida")
elif(x=="CIMITARRA"):
	print(2*S+2*D)
elif(x=="KATANA"):
	print(2*S+D)
elif(x=="SABRE"):
	print(S+2*D)
