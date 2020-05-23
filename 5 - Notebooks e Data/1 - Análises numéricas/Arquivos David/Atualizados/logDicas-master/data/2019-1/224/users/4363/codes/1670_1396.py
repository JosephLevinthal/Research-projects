a = float(input("valor consumido:"))
if (a<=300):
 b = a+a*(10/100)
else:
 b = 0
if (a>300):
	b = a+a*(6/100)
print(round(b,2))