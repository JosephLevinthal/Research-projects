x=float(input("Digite o valor incial da posicaoo: "))
t=0
H=1
z=0
while(H>0):
	H=x-(1/2*(9.8*t**2))
	if(H<=0):
		z=54
	else:	
	   print("t =",t)
	   print("h =",(round(H,1)))
	   t=t+1

	
	
	