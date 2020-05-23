a=int(input("quantidade inicial de copias: "))
b=int(input("quantidade inicial de leucocitos: "))
c=int(input("percentual virus: "))
d=int(input("percentual leucocitos: "))
dia=0
while(b<a*2):
	a=a+(a*(c/100))
	b=b+(b*(d/100))
	dia=dia+1
print(dia)	