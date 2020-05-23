p = int(input("quantidade de tambaquis: "))
c = int(input("crescimento ao ano: "))
v = int(input("quantidade de peixes para a venda: "))
lim = 12000
t = 0
while (0 < p) and (p < 12000): 
	p = p + c*p/100 - v
	t = t + 1
if (p <= 0):
	print("EXTINCAO")
	print(t)
elif (p >= 12000):
	print("LIMITE")
	print(t)