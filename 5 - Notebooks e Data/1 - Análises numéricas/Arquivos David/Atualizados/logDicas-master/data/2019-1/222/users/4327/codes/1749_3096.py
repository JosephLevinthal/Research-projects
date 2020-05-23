num = int(input("posição: "))

while(num >= 0):
	
	if(num == 1):
		pri=num * 20
		ptotal1=ptotal1+pri
		
	elif(num == 2):
		sec=(num/2)*15
		ptotal2=ptotal2+sec
		
	elif(num == 3):
		tri=(num/3)*10
		ptotal3=ptotal3+tri
		
	elif(num >= 4 and num<= 11):
		ret= 11-num
		ptotal4=ptotal4+ret
		
	elif(num>11):
		neu=num*0
		
total=ptotal1+ptotal2+ptotal4+ptotal4+neu

print(total)


		
			
			
	
		
		
			
			

		