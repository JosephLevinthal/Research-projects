t = float(input("meses:"))
h = 1042000/1500
i = (h**(1/t))-1 

if( i <= 0.01):
	print(round(i,5))
	print("Real")
else:
	print(round(i,5))
	print("Irreal")