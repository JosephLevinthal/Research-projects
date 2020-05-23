from numpy import*
t=array(eval(input("Digite o tabuleiro: ")))
m=input("Movimentos: ")
x=0
y=0
n=0
l=100
for i in m:
	j=x
	p=y
	if i=="A":
		x=x-1
	elif i=="D":
		x=x+1
	elif i=="W":
		y=y-1
	elif i=="S":
		y=y+1

	if(y<0)or(x<0):
		y=p
		x=j
	elif (y>shape(t)[1])or(x>shape(t)[0]):
		y=p
		x=j
	print(i)	

	print(y,x)	
	
	
	
print(x)
print(y)
print(n)
print(l)


