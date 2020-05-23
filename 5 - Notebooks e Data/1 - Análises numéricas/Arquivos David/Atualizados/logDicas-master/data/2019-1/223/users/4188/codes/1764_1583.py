a=str(input("digite: "))
p = 0
copia = ""
while(p < len(a)):
	if (len(a)>=2 and len(a)%3==0):
		x = a[p:p+3]
		if p < len(a)-3:
			copia = copia + x + "."
		else:
			copia = copia + x
		p = p + 3
print(copia)