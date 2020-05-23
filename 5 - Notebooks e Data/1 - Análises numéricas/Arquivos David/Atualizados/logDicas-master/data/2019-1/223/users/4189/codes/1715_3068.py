arma = input("arma:").upper()
d = int(input("d:"))
dado1 = int(input("dado1:"))
dado2 = int(input("dado2:"))
s=(dado1+dado2)
if((dado1<1)or(dado2<1)or(d<0)):
	 print("Entrada Invalida")
elif(arma=="CIMITARRA"):
	 print(2*s+2*d)
elif(arma=="KATANA"):
	 print(2*s+d)
elif(arma=="SABRE"):
	 print(s+2*d)
else:
	 print("Entrada Invalida")