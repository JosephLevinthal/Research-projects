from numpy import*
x=array(eval(input("Digite os tamanhos: ")))
h=0
a=0
b=0
c=0
while(len(x)>h):
	if(x[h]>=10):
		a=a+1
		h=h+1
	elif(x[h]>=5)and(x[h]<10):
		b=b+1
		h=h+1
	else:
		c=c+1
		h=h+1
print(a)
print(b)
print(c)
