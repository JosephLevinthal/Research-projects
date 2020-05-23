from numpy import*
x=int(input("numero: "))
print("*"*(x*2))
f="*"
h="o"
t=2
j=1
g=x
while (x>j):
	g=g-1
	n=(f*g+h*t+f*g)
	print (n)
	t=t+2
	j=j+1