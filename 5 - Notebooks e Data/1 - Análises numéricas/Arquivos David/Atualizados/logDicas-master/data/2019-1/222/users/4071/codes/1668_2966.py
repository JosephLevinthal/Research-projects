a=input("S para mulheres ou N para nao mulheres:")
b=int(input("leia o preco:"))
c=int(input("leia a quantidade:"))
total= b*c
if(a=="S"):
	desconto=b*20/100
	total1=total-desconto
	print(round(total1, 2))
else:
	total1=total
	print(round(total1,2))
