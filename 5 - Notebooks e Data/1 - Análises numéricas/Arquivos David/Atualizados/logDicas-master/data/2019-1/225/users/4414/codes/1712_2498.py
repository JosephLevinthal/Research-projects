na=int(input("na:"))
nb=int(input("nb:"))
pa=float(input("pa:"))
pb=float(input("pb:"))

A=na+((na*pa)/100)
B=nb+((nb*pb)/100)

t=1

while(A<B):
	A=A+((A*pa)/100)
	B=B+ ((B*pb)/100)
	t=t+1
print(t)	
	