from math import*

t = float(input("meses: "))

Qf = 1000042
Qo = 1500

i = ((Qf//Qo)**(1/t)) - 1

print(round(i,5))

if(i<=0.01):
	print("Real")

else:
	print("Irreal")