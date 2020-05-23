a = float(input("digite a: "))
b = float(input("digite b: "))
c = float(input("digite c: "))
d = float(input("digite d: "))
e = float(input("digite e: "))
f = float(input("digite f: "))

p1 = c*e - b*f
p2 = a*f - c*d
pb = a*e - b*d


if  (pb != 0):
      x = p1/pb
	   y = p2/pb
		print(x)
		print(y)
		
else:
	 print("Nao tem solucao")
