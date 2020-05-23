b = str(input("C ou F: "))
a = float(input("valor da temp.: "))
f = a*9/5+32
c = 5/9*(a-32)

if b == "C":
	print(f)
else: 
	print(c)