x = float(input("insira x: "))

if(x <= -1 or x >= 1):
	f = x ** 2
else:
	if(-1 < x and x < 0 or 0 < x and x < 1):
		f = x
	else:
		if(x == 0):
			f = 1
	
print(round(f, 4))