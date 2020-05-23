val = float(input("conta: "))
if(val<=300):
	total=val+val/10
	print(round(total, 2))
else:
	total=val+((val/100)*6)
	print(round(total, 2))