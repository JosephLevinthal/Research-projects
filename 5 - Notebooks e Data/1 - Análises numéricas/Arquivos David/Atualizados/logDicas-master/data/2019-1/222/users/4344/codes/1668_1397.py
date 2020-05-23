area = float(input("leia a area a ser fertilizada: "))
h = area*1000
if(area<=10000):
	c = (area*h*5)
print(round(c ,2))
	
else:
   d =(10000*h*5)+(4*h*c)
	print(round(d ,2))