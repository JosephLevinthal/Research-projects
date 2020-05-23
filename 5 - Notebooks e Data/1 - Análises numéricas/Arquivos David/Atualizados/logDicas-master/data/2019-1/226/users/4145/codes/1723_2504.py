v = int(input("quantidade de virus: "))
l = int(input("quantidade de leucocitos: "))
pv = int(input("percentual dos virus: "))/100
pl = int(input("percentual dos leucocitos: "))/100
s=0
d=0
while(l<(2*v)):
	v = v+ pv*v
	l = l+ pl*l
	d = d+1
print(d)	