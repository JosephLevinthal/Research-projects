n= int(input("insira um numero: "))
s=0
d=1
while d<n:
	y=n%d
	if (y==0):
		print(d)
		s=s+d
	d=d+1
if s==n:
	print("PERFEITO")
elif s!=n:
	print("NAO PERFEITO")