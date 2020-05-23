a = int(input("numero:"))
b = int(input("numero:"))
c = int(input("numero:"))

if(a>b>c):
	print(b)
elif(b>c>a):
	print(c)
elif(a<b<c):
	print(b)
elif(b<c<a):
	print(c)
else:
	print(a)