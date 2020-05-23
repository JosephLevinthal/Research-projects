from numpy import*
c1=float(input("valor compra 1: "))
c2=float(input("valor compra 2: "))
c3=float(input("valor compra 3: "))
c4=float(input("valor compra 4: "))

s = c1 + c2 + c3 + c4
s = array(c1,c2,c3,c4)

if (s > 80):
	cd = (s*0.15)
	cf = s - cd
else:
	cf = s

print(round(cf,2))