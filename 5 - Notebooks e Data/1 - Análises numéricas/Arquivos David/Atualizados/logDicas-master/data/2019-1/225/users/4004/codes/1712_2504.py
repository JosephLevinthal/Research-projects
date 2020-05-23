v = int(input("quantidade do virus: "))
l = int(input("quantidade de leucocitos: "))
pv = float(input("percentual de crescimento do virus: "))
pl = float(input("percentual de crescimento do leucocitos: "))

t = 0

while ((l / v) <= 2):
	v = v + (v * (pv/100))
	l = l + (l * (pl/100))
	t = t + 1
print(t)