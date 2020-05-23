qt=int(input("pirarucu:"))
pc=float(input("crescimento:"))


c=0

while(qt < 8000 and qt > 0):
	v = int(input("vendas:"))
	qt = qt+((qt*pc)/100)- v
	c = c + 1
	 
if(qt>=8000):
	print("MAXIMO")
elif(qt<=0):
	print("ZERO")
print(c)	
	

	