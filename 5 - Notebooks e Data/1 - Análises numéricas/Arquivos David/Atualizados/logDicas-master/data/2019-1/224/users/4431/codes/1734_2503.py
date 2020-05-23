x=int(input("digite um numero: "))
h=1
j=0
z=0
d=1
while(j<x):
	z=z+(4/h*d)
	h=h+2
	d=-d
	j=j+1
print(round(z,8))	