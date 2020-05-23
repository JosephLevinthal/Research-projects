x = float(input("valor de x: "))

if(-100 <= x and x < 0):
	print(round(-1/x, 4))
elif(0 < x and x <= 100):
	p = 1 / x
	r = round(p, 4)
	print(r)
else:
	if(x > 100 or x < -100 or x == 0):
		print("entrada invalida")