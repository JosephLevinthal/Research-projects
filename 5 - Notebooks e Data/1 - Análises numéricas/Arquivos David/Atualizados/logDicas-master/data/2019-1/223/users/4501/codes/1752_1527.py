a=int(input("quntidade inicial Forseti: "))
b=int(input("quantidade inicial Loki: "))
c=float(input("% Forseti: "))
d=float(input("% Loki: "))
anos=0
while(a>b):
	a=a+a*(c/100)
	b=b+b*(d/100)
	anos=anos+1
print(anos)	