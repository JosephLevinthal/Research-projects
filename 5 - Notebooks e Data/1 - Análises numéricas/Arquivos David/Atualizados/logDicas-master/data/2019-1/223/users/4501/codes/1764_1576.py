from numpy import*
a=array(eval(input("v1: ")))
b=array(eval(input("v2: ")))
i=0
x=0
y=0
while(i<size(a)):
	if(a[i]==11):
		if(b[i]==22):
			y=y+1
		elif(b[i]==33):
			x=x+1
	elif(a[i]==22):
		if(b[i]==11):
			x=x+1
		elif(b[i]==33)	:
			y=y+1
	elif(a[i]==33)	:
		if(b[i]==11):
			y=y+1
		elif(b[i]==22)	:
			x=x+1
	i=i+1
print(size(a))	
if(sum(x)>sum(y)):
	print("EUSAPIA")
elif(sum(x)<sum(y)):
	print("BARSANULFO")
else:
	print("EMPATE")

	
		
	