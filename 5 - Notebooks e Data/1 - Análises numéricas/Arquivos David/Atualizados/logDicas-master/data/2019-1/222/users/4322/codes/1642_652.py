n=int(input())

if (n % (n - (n//100)*100)==0):
	print ("SIM")
else:
	print ("NAO")