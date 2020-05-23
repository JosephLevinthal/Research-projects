escala=input("CELSIUS ou FAHRENHEIT? (C/F)")
temp=float(input("temperatura"))
f=(5/9)*(temp-32)
c=(9/5*temp)+32
if (escala=="C"):
	print(round(c,2))
else:
	print(round(f,2))