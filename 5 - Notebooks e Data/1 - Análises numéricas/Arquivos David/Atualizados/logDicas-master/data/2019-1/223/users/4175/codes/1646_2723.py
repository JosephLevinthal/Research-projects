a = int(input())
b = int(input())
c = int(input())

if (a>b) == True:
	if (a>c) == True:
		if(b>c) == True or (b>c) == False:			
			print(a)
				
if (a>b) == False:
	if (a>c) == True or (a>c) == False:
		if(b>c) == True:
			print(b)

if (a>b) == True or (a>b) == False:
	if (a>c) == False:		
		if(b>c) == False:			
			print(c)

			