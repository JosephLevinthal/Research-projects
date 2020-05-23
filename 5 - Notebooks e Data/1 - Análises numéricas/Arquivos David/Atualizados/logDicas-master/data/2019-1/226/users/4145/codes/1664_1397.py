a = int(input("area a ser fertilizada em hectares: "))
ex = a - 10000
if(ex <= 0):
	cal = 5.00 * a
else:
	cal = 5 * (a - ex) + (ex) * 4 
print(round(cal,2))