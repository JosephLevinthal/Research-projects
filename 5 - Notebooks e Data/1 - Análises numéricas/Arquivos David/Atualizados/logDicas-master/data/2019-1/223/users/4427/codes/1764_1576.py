from numpy import*
a=array(eval(input("")))
b=array(eval(input("")))

i=0
EU=0
BA=0

while(i<size(a)):
	if(a[i]==11 and b[i]==11 or a[i]==22 and b[i]==22 or a[i]==33 and b[i]==33):
		EU=EU+0
		BA=BA+0
	elif(a[i]==11 and b[i]==33 or a[i]==22 and b[i]==11 or a[i]==33 and b[i]==22):
		EU=EU+1
		BA=BA+0
	elif(b[i]==11 and a[i]==33 or b[i]==22 and a[i]==11 or b[i]==33 and a[i]==22):
		EU=EU+0
		BA=BA+1
	i=i+1
print(i)
if(EU==BA):
	print("EMPATE")
if(EU>BA):
	print("EUSAPIA")
elif(EU<BA):
	print("BARSANULFO")