p = int(input("Quantidade de tambaquis:"))
c = int(input("Crescimento ao ano:"))
v = int(input("quabtidade de peixes para :"))
lim = 12000
t = 0
while (0<p)and (p<12000):
	p = p+ c*p/100 -v
	t = t+1
if (p<= 0):
	print("EXTINCAO")
	print(t)
elif (p >= 12000):
	print("LIMITE")
	print(t)