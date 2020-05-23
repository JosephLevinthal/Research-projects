b = int(input(" Digite o numero 1: "))
c = int(input(" Digite o numero 2: "))
d = int(input(" Digite o numero 3: "))

if(b<c and b<d):
	menor=b
if(c<b and c<d):
	menor=c
if(d<b and d<c):
	menor=d
print(menor)

