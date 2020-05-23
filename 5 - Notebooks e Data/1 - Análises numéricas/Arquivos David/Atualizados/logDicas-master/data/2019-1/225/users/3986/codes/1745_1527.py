q1=int(input("quantidade inicial de forseti :"))
q2=int(input("quantidade inicial de loki :"))
p1=float(input("percentual anual de crescimento de forseti :"))
p2=float(input("percentual anual de crescimento de loki :"))
t=0
x=q1
y=q2

while (p2 > p1) :
	t=t + 1
	x=x+(x*(p1/100))
	y=y+(y * ( p2 / 100))
	
print(y)