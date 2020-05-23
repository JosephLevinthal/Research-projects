from numpy import*
x=int(input("Digite um numero: "))
m=arange(x+1)
h=-1
for i in m:
	f="*"
	f=f*m[h]
	print(f)
	h=h-1

for i in range(1,x+1):
	f="*"
	f=f*i
	print(f)
	