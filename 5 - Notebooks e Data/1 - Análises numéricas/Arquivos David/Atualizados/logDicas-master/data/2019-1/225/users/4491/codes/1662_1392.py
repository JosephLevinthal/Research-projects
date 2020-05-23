c = float(input("consumo: ")) 
t1 = 30 + 3*c
t2 = 30 + 3.5*c
if(c <= 10):
	print(round(t1, 2))
else: 
	print(round(t2,2))
	