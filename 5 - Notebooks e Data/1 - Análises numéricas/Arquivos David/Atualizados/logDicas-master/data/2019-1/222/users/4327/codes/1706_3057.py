temp=float(input("tempo: "))

if((temp>=0) and (temp<100)):
	valor = ((temp * 80) + 3000)
	
elif((temp >= 100) and (temp < 200)):
	valor = ((temp * 90) + 4000)

elif((temp>=200) and (temp<300)):
	valor = ((temp * 100) + 5000)
	
elif(temp>300):
	valor = ((temp * 110)+ 6000)

print (round(valor,2))