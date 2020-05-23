p = int(input("quantidade de pirarucus: "))
pc = int(input("percentual de crescimento: "))/100

m=0
while(p>0 and p<8000):
	pr = int(input("pirarucus retirados: "))
	p= p + p*pc -pr
	m=m+1
	#pr = int(input("pirarucus retirados: "))
if(p<=0):
	print("ZERO")
else:	
	print("MAXIMO")
print(m)