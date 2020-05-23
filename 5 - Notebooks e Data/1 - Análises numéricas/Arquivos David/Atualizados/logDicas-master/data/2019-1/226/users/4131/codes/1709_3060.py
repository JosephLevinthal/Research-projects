d1 = int(input("dado 1:"))
d2 = int(input("dado 2:"))
r = int(input("rodada:"))
CONSTRICAO = d1+d2==12
POLEN = d1+d2<5 
FRAQUEZA = 11>=d1+d2>=5
if(CONSTRICAO):
	print("CONSTRICAO")
	print(d1+d2+1)
elif(POLEN):
	print("POLEN")
	print((d1+d2+1)*r)
elif(FRAQUEZA):
	print("FRAQUEZA")
	print(d1*d2)
elif(d1==0)or(d1>6)or(d2==0)or(d2>6):
	print("Entrada invalida")