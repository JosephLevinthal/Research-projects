p=int(input("quantidade inicia: "))
per=float(input("% : "))
c = 0
while(p>0 and p<8000):
	r=int(input("reirado: "))
	p = p + p*(per/100) - r
	c = c + 1
	if(p<=r):
		e="ZERO"
	if(p>=8000):
		e="MAXIMO"
print(e)
print(c)	