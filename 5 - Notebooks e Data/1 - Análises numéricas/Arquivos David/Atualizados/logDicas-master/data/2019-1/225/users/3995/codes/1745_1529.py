k=int(input("infantaria:"))
j=int(input("cavalaria:"))
pk=float(input("percentual infantaria:"))
pj=float(input("percentual cavalaria:"))
l=50000
c=0

while((j+k)<l):
	h=(k*pk)/100
	k=k+h
	y=(j*pj)/100
	j=j+y
	c+=1
print(c)