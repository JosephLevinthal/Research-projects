na=int(input())
nb=int(input())
pa=float(input())
pb=float(input())
anos=0

while (na<nb):
	cresa=na*(pa/100)
	na=na+cresa
	cresb=nb*(pb/100)
	nb=nb+cresb
	anos=anos+1
print(anos)
