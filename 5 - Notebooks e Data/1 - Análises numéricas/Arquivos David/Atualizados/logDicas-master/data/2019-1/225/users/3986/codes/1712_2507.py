q1=int(input("quantidade de pirarucus: "))
p1=int(input("percentual de crecimento mensal: "))
a=q1
t=0
while (a < 8000) and (a > 0 ) :
	t=t + 1
	qv=int(input("quantidade de pirarucus retirados para venda: "))
	a=a + (a * (p1 / 100)) 
	a=a - qv
if (a >= 8000):
	print ("MAXIMO")
else :
	print("ZERO")
print(t)