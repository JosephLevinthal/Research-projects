n = int(input())

a = 0
while(n!=0):
	if(n==1):
		a = 25 + a
	elif(n==2):
		a = 18 + a
	elif(n==3):
		a = 12 + a
	elif(n==4):
		a = (14 - 4) + a
	elif(n==5):
		a = (14-5) + a
	elif(n==6):
		a = (14-6) + a
	elif(n==7):
		a = (14-7)+ a
	elif(n==8):
		a = (14-8) + a
	elif(n==9):
		a = a + (14-9)
	elif(n==10):
		a = a + (14-10)
	else:
		a = a + 0
	n = int(input())
print (a)