from math import*

f = float(input("number:"))

if(f <= 0):
	print("0")
elif(f > 0) and (f <= 1):
	print("1")
elif(f > 1 ) and (f <= 2):
	x = abs(f**(1/2))
	print(round(x,4))		  
else:
	x = abs(f**(1/3))
	print(round(x,4))