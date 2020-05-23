t = int(input("t:"))
i = round(((1042000/1500000)**(1/t)-1,5)

if(i <= 0.01):
	print("REAL")	
else:
	print("IRREAL")