a = int(input("nmr: "))
b = (a-(a//100)*100)
if a%b == 0:
	print("SIM")
else:
	print("NAO")