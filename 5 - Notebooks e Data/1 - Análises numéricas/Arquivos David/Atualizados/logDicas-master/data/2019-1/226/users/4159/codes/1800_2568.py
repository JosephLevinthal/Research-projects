n = int(input("numero de repeticao: "))
a ="o"*n*2
b = "*"*n*2
r =""
f = n
while f>0:
	r = a +b[0,f-1] +b[f,-1]
	f=f-1
	print(r)
	