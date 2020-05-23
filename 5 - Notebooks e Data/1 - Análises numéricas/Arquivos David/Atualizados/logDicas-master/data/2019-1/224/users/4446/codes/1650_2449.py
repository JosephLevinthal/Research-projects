a=float(input("digite a: "))
b=float(input("digite b: "))
c=float(input("digite c: "))
d=float(input("digite d: "))
e=float(input("digite e: "))
f=float(input("digite f: "))

k=(a * e - b * d)
w=(c * e - b * f)
q=(a * f - c * d)

if (k == 0):
	print("Nao tem solucao")
else:
	x= w / k
	y= q / k
	print(x)
	print(y)