atk=input("atk:")
D1=int(input("d1:"))
D2=int(input("d2:"))
D3=int(input("d3:"))
D4=int(input("d4:"))
x==ESPADA
Y==CAU
if(atk == "X" and (D1>=1 ) and (D1<=6) ):
	print((D1+6)+ (D2+6)+ (D3+6))
else:
	print("Entrada invalida")
if(atk== "y" and (D1>=1) and (D1<=6) and (D2>=1) and (D2<=6) and (D3>=1) and (D3<=6) and (D4>=1) and (D4<=6)):
	print((D1+D2+D3)*D4)	