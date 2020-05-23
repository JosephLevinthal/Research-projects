from numpy import *
num=input("digite: ")
x=int(num)
i=0
k=3
msg=""
while(i<len(num)):
	if(i==(len(num)-3)):
		msg=msg+num[i:k]
		i=i+3
		k=k+3
	else:
		msg=msg+num[i:k]+"."
		i=i+3
		k=k+3
print(msg)