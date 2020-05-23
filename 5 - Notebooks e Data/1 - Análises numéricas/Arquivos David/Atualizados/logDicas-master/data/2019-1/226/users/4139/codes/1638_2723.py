a = int(input("numero:"))
b = int(input("numero:"))
c = int(input("numero:"))

if(a<b):
	if(b<c):
		print(c)
	else:
		print(b)
elif(b<c):
	if(c<a):
		print(a)
	else:
		print(c)
elif(c<a):
	if(a<b):
		print(b)
	else:
		print(a)
