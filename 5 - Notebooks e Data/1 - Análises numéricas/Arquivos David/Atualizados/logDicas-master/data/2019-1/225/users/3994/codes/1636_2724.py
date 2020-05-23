b = int(input(" Digite numero 1: "))
c = int(input(" Digite numero 2: "))
d = int(input(" Digite numero 3: "))
if(b>c and b<d):
	meio=b
if(b<c and b>d):
	meio=b
if(c>b and c<d):
	meio=c
if(c<b and c>d):
	meio=c
if(d>b and d<c):
	meio=d
if(d<b and d>c):
	meio=d
print(meio)