from numpy import*

v1 = array(eval(input("vetor eusapia =" )))
v2 = array(eval(input("vetor barsanulfo =" )))

i = 0
e = 0
b = 0

while (i < size(v1)):
	if(v1[i] == 22 and v2[i] == 11 or v1[i] == 11 and v2[i] == 33
	  or v1[i] == 33 and v2[i] == 22):
		e = e + 1
	elif(v2[i] == 22 and v1[i] == 11 or v2[i] == 11 and v1[i] == 33
	  or v2[i] == 33 and v1[i] == 22):
		b = b + 1
	else:
		b = b + 0
		e = e + 0
	i=i+1
print(i)	  
if(b > e):
	print("BARSANULFO")
elif(e > b):
	print("EUSAPIA")
else:
	print("EMPATE")