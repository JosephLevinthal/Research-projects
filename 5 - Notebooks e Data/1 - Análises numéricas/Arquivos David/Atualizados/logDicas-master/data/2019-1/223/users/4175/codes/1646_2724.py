a = int(input())
b = int(input())
c = int(input())

if (a>b) == False:
	if (a>c) == True:
		if(b>c) == True:
			print(a)
if (a>b) == True:
	if (a>c) == False:
		if (b>c) == False:
			print(a)

if (a>b) == True:
	if (a>c) == True:
		if(b>c) == True:
			print(b)
			
if (a>b) == False:
	if (a>c) == False:
		if(b>c) == False:
			print(b)

if (a>b) == True:
	if (a>c) == True:
		if(b>c) == False:
			print(c)

if (a>b) == False:
	if (a>c) == False:
		if(b>c) == True:
			print(c)
			