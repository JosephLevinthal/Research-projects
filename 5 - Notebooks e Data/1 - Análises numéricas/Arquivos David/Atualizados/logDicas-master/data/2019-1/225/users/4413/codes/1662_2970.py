t = int(input("tempo: "))
Qf = 1042000.00 
Qo = 1500.00
i = round(((Qf/Qo)**(1/t)) - 1, 5)
print(i)
if(i<=0.01):
	msg = ("Real")
else:
	msg = ("Irreal")
print(msg)