a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))
d = float(input("Digite d: "))
e = float(input("Digite e: "))
f = float(input("Digite f: "))
z = (a * e) - (b * d) 

x = ((c * e) - (b * f)) 
y = ((a * f) - (c * d)) 

if(z == 0):
	print("Nao tem solucao")
else:
	print(((c * e) - (b * f)) / z)
	print(((a * f) - (c * d)) / z)
	
