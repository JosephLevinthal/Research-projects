from math import*
x = float(input())

if (x>=-1 and x<-0.5) or (x>0.5 and x<=1):
	fx = asin(x)
	fx = degrees(fx)
	print(round(fx,2))
elif x>=-0.5 and x<=0.5:
	fx = acos(x)
	fx = degrees(fx)
	print(round(fx,2))
else:
	print("entrada invalida")