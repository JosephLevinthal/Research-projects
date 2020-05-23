ac=int(input())

if (ac<0):
	print("area invalida")
elif (ac>=0 and ac<=100):
	valor=ac*2 + 100
	print(round(float(valor),2))
elif (ac>100 and ac<=2500):
	valor=ac*1.8 + 150
	print(round(float(valor),2))
elif (ac>2500 and ac<=10000):
	valor=ac*1.5 + 200
	print(round(float(valor),2))
else:
	valor=ac*1.2 + 250
	print(round(float(valor),2))