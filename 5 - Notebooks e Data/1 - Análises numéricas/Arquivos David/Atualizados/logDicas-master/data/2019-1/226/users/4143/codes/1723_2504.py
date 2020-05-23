v = int(input("virus:"))
l = int(input("leucocitos:"))
pv = int(input("multiplicador do virus:"))
pl = int(input("multiplicacao dos leucocitos:"))
t =0
while (2*v >= l):
	v = v*(1+(pv/100))
	l = l*(1+(pl/100))
	t = t+1
print(t)