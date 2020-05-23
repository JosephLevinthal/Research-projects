x = float(input(""))

if (- 1000 <= x) and (x<-2):
	f = - 1/(x+2)
	print(round(f,4))
elif (2 < x) and (x<=1000):
	f = 1/(x-2)
	print(round(f,4))
else:
	print("entrada invalida")
