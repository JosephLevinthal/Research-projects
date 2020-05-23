a = input()
d = int(input())
v1 = int(input())
v2 = int(input())

if(a=="CIMITARRA" and v1<=10 and v1>=1 and v2>=1 and v2<=10 and d>=0):
	dano = (2*(v1+v2)) + (2*d)
	print(dano)
elif(a=="KATANA" and v1<=10 and v1>=1 and v2<=10 and v2>=1 and d>=0):
	dano = 2*(v1+v2) + d
	print(dano)
elif(a=="SABRE" and v1<=10 and v1>=1 and v2<=10 and v2>=1 and d>=0):
	dano = (v1+v2) + 2*d
	print(dano)
else:
	print("Entrada invalida")

	