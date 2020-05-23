from math import*

x = float(input("Digite x: "))

if(x>=-1 and x<(-1/2) or x>(1/2) and x<=1):
	print(round(degrees(asin(x)),2))
elif(x>=-1/2 and x<=1/2):
	
	print(round(degrees(acos(x)),2))
else:
	print("entrada invalida")