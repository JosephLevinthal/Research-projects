num = int(input())
if 100 <= num <= 999 and num %(num - 100*(num//100)) == 0:
	print("SIM")
else:
	print("NAO")