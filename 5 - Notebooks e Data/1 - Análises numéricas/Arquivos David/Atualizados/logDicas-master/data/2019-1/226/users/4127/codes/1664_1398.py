t= float(input("qual o tempo de voo? "))
exc= t-200
if (t<=200):
	print(5000+100*t)
else:
	print(8000+100*200+(exc*90))