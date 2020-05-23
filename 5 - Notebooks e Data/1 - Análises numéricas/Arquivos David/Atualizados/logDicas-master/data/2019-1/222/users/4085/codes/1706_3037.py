x = float(input("escreva o valor de x: "))
if (x <= -1) or (x >=1):
	f = x **2
	print (round(f, 4))
elif ((x < 0) and (x > -1) or (x > 0) and (x < 1)):
	f = x
	print (round(f, 4))
else:
	f = 1
	print (round(f, 4))