num = int(input("numero de tres d:"))

n1 = num - (num//100)*100

if(num % n1 == 0 ):
	print("SIM")
else:
	print("NAO")
	
