x = input("OLHA O PASTELLLL:").upper()
y = x.replace(" ","")
i = -1
inv =""
while( i >= -len(y)):
	inv = inv + y[i]
	i = i - 1
if(inv == y):
	print(y)
	print("1")
else:
	print(y)
	print("0")
		
		