a=int(input("numero1:"))
b=int(input("numero2:"))
c=int(input("numero3:"))
if(a<b and a<c):
	menor=a
if(b<a and b<c):
	menor=b
if(c<a and c<b):
	menor=c
print(menor)