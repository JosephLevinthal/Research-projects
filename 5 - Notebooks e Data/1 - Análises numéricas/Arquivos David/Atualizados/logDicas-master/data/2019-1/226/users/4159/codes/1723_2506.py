tam = int(input("peixe "))
p = int(input("nasce "))/100
v = int(input("vende"))
f = 0
while(tam>0 and tam<12000):
	tam = tam +tam*p
	tam = tam - v
	f =f+1
	if(tam<=0):
		c="EXTINCAO"
	else:
		c="LIMITE"
print(c)
print(f)