x=input("L ou S")
y=int(input("quantidade de salgado ou lanches: "))
z=int(input("quantidade de refrigerante: "))
l=5.00
s=3.50
r=4.0

if(x.upper() == "L"):
	total= (l*y+r*z)
else:
	total= (s*y+r*z)
print(round(total,2))
