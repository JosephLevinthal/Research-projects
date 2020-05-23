compra = float(input())
if (compra >= 200.00):
	total = compra - compra*0.05
else:
	total = compra
print(round(total,2))