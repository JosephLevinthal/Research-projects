x = float(input("Determine x: "))

if ((x<=-1) or (x>=1)):
	print(round(x*x, 4))
elif ((x>-1 and x<0) or (x>0 and x<1)):
	print(round(x, 4))
elif (x==0):
	print(round(1, 4))