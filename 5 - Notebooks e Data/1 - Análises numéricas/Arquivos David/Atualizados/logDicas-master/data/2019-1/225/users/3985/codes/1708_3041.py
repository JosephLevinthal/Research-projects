x= float(input("VALOR:"))

fx1= (-1/(x+2))
fx2= (1/(x-2))

if (x=>-1000) and (x<-2):
	g= fx1
	p= round(g,4)
	print(p)
elif (x>2) and (x<=1000):
	g= fx2
	p= round(g,4)
	print(p)