qi=int(input("peixe:"))
pc=float(input("crescimento:"))
qv=int(input("vendas:"))

c=0
while(qi<12000 and qi>0):
	qi=qi+((qi*pc)/100)- qv
	c=c+1
	
if(qi>=12000):
	print("LIMITE")
else:
	print("EXTINCAO")
	
print(c)	
	