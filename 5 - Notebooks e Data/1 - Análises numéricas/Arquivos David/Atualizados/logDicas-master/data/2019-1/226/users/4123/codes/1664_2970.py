t = float(input())
i = (1042000/1500)**(1/t)-1
print(round(i,5))
if i <=0.01:
	print("Real")
else:
	print("Irreal")