cons= float(input("digite o consumo de agua em m3: "))
if(cons<10):
	v1=30+cons*3
	print(round(v1,2))
else:
	v2=30+cons*3.5
	print(round(v2,2))