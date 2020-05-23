d1=int(input())
d2=int(input())
rd=int(input())
if(d1<=0 or d1>6 or d2<=0 or d2>6 or rd<0):
	print("Entrada invalida")
else:
	if((d1+d2)==12):
		print("CONSTRICAO")
		print("13")
	elif((d1+d2)<5):
		print("POLEN")
		dano=(d1+d2+1)*rd
		print(dano)
	else:
		print("FRAQUEZA")
		dano=d1*d2
		print(dano)