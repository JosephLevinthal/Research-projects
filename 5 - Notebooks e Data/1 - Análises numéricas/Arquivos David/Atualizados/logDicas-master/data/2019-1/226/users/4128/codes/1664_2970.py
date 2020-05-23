

t = int(input("meses"))
qf = 1042000
qo = 1500

i = (qf/qo)**(1/t) -1

if(i <= 0.01):
	print(round(i,5))
	print("Real")
else:
	print(round(i,5))
	print("Irreal")