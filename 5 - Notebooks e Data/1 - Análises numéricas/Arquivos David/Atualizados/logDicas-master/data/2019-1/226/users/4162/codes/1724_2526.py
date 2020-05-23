n1= int(input("insira um numero: "))
n2= int(input("insira um numero: "))
d1=1
d2=1
s1=0
s2=0
while d1<n1:
	y1=n1%d1
	if (y1==0):
		s1=s1+d1
	d1=d1+1
while d2<n2:
	y2=n2%d2
	if (y2==0):
		s2=s2+d2
	d2=d2+1
print(s1)
print(s2)
if (s1==n2)and(s2==n1):
	print("AMIGOS")
else:
	print("NAO AMIGOS")