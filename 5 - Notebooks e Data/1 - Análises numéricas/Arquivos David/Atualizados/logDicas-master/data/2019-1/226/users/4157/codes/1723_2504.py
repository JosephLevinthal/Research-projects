c = int(input("qnt inicial de copias:"))
l = int(input("qnt inicial de leucocitos:"))
pv = int(input("percentual de virus:"))/100
pl = int(input("percentual de leucocitos:"))/100
d = 0
while(l<(2*c)):
	c = c + pv *c
	l = l+pl*l
	d = d+1
print(d)