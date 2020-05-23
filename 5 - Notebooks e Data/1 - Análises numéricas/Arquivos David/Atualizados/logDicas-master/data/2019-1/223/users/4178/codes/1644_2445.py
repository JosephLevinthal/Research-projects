var1= input("F/C: ")
var2= int(input("Num: "))

if var1 == "F": 
	xx=5/9*(var2-32)
	print(round(xx,2))
else:
	print(var2*1.8+32)
