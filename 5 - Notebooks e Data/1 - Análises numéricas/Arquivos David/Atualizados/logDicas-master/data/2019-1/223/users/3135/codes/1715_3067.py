a=input("Insira o seu ataque (Espada flamejante OU Cauda constritora):").upper()
D1=int(input("D1:"))
D2=int(input("D2:"))
D3=int(input("D3:"))
D4=int(input("D4:"))
cauda=(D1+D2+D3)*D4
if((D1<=0 or D1>6)or(D2<=0)or(D2>6))or(D3<=0 or D3>6)or(D4<=0 or D4>6):
	print("Entrada invalida")
elif(a=="ESPADA"):
	print(2*(D1+D2+D3+D4+6))
elif(a=="CAUDA"):
	print(cauda)
else:
	print("Entrada invalida")
	