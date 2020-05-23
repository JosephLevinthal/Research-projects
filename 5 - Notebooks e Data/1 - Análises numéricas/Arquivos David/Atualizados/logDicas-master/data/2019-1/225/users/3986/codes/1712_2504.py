q1=int(input("quant inicial de copias no sangue: "))
q2=int(input("quant inicial de leucocitos no sangue: "))
p1=int(input("mult do virus: "))
p2=int(input("mult dos leucocitos : "))
x=q1
y=q2
t=0
while ((2*x) > y) and (p1<p2) and (q1>q2):
	t=t+1
	x=x + (x*(p1/100))
	y=y + (y*(p2/100))
print(t)