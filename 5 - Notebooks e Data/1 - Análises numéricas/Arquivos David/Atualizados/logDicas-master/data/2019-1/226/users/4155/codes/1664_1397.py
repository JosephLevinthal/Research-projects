a = float(input("area a ser fertilizada: "))

if(a <= 10000):
	msg = (5 * a)
else:
	msg = (5 * 10000) + (4 * (a - 10000))
	
r = round(msg, 2)
print(r)