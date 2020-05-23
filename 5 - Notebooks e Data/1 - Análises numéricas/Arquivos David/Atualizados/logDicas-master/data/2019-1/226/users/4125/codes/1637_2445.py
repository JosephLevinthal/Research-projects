x = (input(" digite:"))
v = float(input("digite a temp: "))
c = (5/9)*(v-32)
f = (v*(9/5) + 32)
if (x.upper() == "F"):
	x1 = c
else:
	x1 = f

print(round(x1,2))