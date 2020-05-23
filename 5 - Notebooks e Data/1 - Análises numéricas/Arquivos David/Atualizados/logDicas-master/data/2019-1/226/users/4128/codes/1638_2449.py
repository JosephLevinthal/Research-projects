a = float(input("aa:"))
b = float(input("bb:"))
c = float(input("cc:"))
d = float(input("dd:"))
e = float(input("ee:")) 
f = float(input("ff:")) 

if((a*e)-(b*d) != 0):
	x = ((c*e)-(b*f))/((a*e)-(b*d))
	y = ((a*f)-(c*d))/((a*e)-(b*d)) 
	print(x)
	print(y)
else:
	print("Nao tem solucao")