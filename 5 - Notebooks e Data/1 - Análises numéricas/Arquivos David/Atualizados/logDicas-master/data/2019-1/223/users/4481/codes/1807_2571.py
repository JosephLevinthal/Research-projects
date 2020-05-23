from numpy import*

a=input('string vazia: ')
b=''
for i in range(len(a)):
	if(a[i].upper()!='A'):
		b=b+a[i]
print(b)