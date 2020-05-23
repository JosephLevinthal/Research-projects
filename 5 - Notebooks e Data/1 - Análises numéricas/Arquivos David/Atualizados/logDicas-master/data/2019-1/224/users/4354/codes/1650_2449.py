a = float(input("digite a : "))
b = float(input("digite b : "))
c = float(input("digite c : "))
d = float(input("digite d : "))
e = float(input("digite e : "))
f = float(input("digite f : "))
if(a * e - b * d != 0) :
	x = (c * e - b * f) / (a * e - b * d)
	y = (a * f - c * d) / (a * e - b * d) 
	print(x)
	print(y)
else :
	print("Nao tem solucao")	
