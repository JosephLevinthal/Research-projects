x=int(input("numero:"))
y=int(input("sorteado:"))
d1=x%10
d2=x//10
d3=y%10
d4=y//10
if(x==y):
	print("Ganhou R$ 100.000,00 ")
elif((d1==d4) and (d2==d3)):
	print("Ganhou R$ 50.000,00")
elif(d1==d3 or d1==d4 or d2==d3 or d2==d4):
	print("Ganhou R$ 1.000,00")
else:
	print("Perdeu")