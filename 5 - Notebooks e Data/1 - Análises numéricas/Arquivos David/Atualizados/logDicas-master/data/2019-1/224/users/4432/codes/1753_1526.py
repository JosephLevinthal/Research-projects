a=int(input("quantidade inicial de mana da bruxa sosipatra"))
b=int(input("quantidade de mana que ela gasta por dia para sustentar"))
c=int(input("mana que ela recupera  "))
cont=0
acu=0
while(a>0):
	cont=cont+1
	a=a-b+c
print(cont)
		  