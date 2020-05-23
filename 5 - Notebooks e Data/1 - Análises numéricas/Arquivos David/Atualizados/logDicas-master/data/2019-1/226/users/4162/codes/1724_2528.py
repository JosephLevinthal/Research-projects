n= int(input( "insira um numero: "))
while n>0:
	a=(n//100)
	b=(n//10%10)
	c=(n%10)
	print(a,b,c)
	if a+b+c==a or a+b+c==b or a+b+c==c:
		h=1
	elif a+b+c==a+b or a+b+c==b+c or a+b+c==a+c:
		h=2
	else:
		h=3
	s=a**h+b**h+c**h
	print(s)
	if s==n:
		print("ARMSTRONG")
	else:
		print("NAO ARMSTRONG")
	n= int(input( "insira um numero: "))
	