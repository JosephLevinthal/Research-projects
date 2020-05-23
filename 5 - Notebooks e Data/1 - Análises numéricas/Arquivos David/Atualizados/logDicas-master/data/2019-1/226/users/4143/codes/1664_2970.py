a = int(input("Meses:"))
eq = ((1042000/1500)**(1/a)) - 1
print(round(eq,5))
if (eq<=0.01):
	print("Real")
else:
	print("Irreal")