a=float(input("qual a area a ser fertilizada ? "))
if((a>=0) or (a<=10000)):
	print(round(a * 6 + 100, 2))
elif((a>=10001) or (a<=20000)):
	print(round(a * 5.5 + 150, 2))
elif((a>=20001) or (a<=30000)):
	print(round(a * 5 + 200, 2))
elif(a>=30001):
	print(round(a * 4,5 + 250, 2))

