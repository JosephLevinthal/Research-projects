qsu = int(input())
qsal = int(input())
saldo = float(input())
total = (qsu * 3) + (qsal * 3.50)
if (total>saldo):
	print(round(total,2))
	print("Nao")
	
else:
	print(round(total,2))
	print("Sim")
	