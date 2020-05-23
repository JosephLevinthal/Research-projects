na=int(input("numero apostado: "))
ns=int(input("numero sorteado: "))

x=na//10
y=na%10
x1= ns//10
y1=ns%10

if(x==x1 and y== y1):
	print("Ganhou R$ 100.000,00")
elif(x==y1 and y== x1):
	print("Ganhou R$ 50.000,00")
elif(x==x1 or x==y1 or y==x1 or y==y1):
	print("Ganhou R$ 1.000,00")
else:
	print("Perdeu")