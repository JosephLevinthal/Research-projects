from math import*
x = float(input("valor de x:"))
if(((x>= -1 ) and(x<-1/2)) or ((x>1/2) and (x<=1))):
	fx = degrees(asin(x))
	print(round(fx,2))
elif((x>=-1/2) and (x<=1/2)):
	fx = degrees(acos(x))
	print(round(fx,2))
else:
	print("entrada invalida")
  