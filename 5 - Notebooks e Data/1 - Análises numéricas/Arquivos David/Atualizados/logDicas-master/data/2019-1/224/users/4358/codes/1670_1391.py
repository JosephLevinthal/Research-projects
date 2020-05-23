vr1=float(input("Digite o consumo energetico(kwh):"))
custo1=(0.60*vr1)+5
custo2=(0.75*vr1)+16
if(vr1<=150):
	print(round(custo1,2))
else:
	print(round(custo2,2))
	