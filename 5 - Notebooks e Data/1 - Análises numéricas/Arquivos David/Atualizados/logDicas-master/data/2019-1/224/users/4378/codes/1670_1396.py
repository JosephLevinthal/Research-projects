vc=float(input("digite o valor consumido:"))
x= 0.1 * vc + vc
y= 0.06 * vc + vc
if vc<=300:
   print(round(x, 2))
else:
	print(round(y, 2))