a=float(input(""))
b=float(input(""))
r=float(input(""))
x=0
y=0

Q1=a>x and b>y
Q2=b>y and a<x
Q3=a<x and b<y
Q4=b<y and a>x


if(a and b >Q1 or a and b>Q2 ):
	d="Superiores"
else:
	d="Inferiores"
print(d)