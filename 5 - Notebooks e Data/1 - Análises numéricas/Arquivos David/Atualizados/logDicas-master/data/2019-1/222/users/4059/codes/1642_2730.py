x=float(input())
y=float(input())

if (x>0 and y>0) or (x<0 and y>0):
	print("Superiores")
if (x>0 and y<0) or (x<0 and y<0):
	print("Inferiores")