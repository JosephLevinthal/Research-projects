p=float(input("valor do peso: "))
if((p>0)and(p<5000)):
	print(round((p*0.03)+20, 2))
elif((p>5000)and(p<6000)):
	print(round((p*0.04)+25, 2))
elif((p>6000)and(p<7000)):
	print(round((p*0.05)+30, 2))
elif((p>7000)):
	print(round((p*0.06)+35, 2))