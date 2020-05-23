t = float(input("qual o periodo de tempo: "))
Qf = (1042000)
Qo = (1500)
i = ((Qf/Qo)**(1/t)) - 1
print(round(i ,5))
if(i <= 0.01):
	print("Real")
else:
	print("Irreal")