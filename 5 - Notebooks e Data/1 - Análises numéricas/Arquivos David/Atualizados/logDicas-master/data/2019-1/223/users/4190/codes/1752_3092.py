y = 0
p = input('c: ').upper()
while (p!="X"):
	p = input('c: ').upper()
	if (p=='V'):
		y = y+3
	elif (p=='E'):
		y = y+2
	elif (p=='D'):
		y = y+1
	else:
		y = y+0
	
y = y/100
print(round(y, 2))
